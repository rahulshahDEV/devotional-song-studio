#!/usr/bin/env python3
"""Validate reviewed song timing and compile absolute frame cues plus SRT."""

import argparse
from fractions import Fraction
import json
import math
from pathlib import Path

from sync_common import atomic_json, atomic_text, finite, fingerprint, local_path, output_path, video_root


def frame_at(seconds, fps):
    return math.floor(Fraction(str(seconds)) * fps + Fraction(1, 2))


def timestamp(seconds):
    total = math.floor(seconds * 1000 + 0.5)
    hours, rest = divmod(total, 3600000)
    minutes, rest = divmod(rest, 60000)
    sec, ms = divmod(rest, 1000)
    return f'{hours:02}:{minutes:02}:{sec:02},{ms:03}'


def intervals(items, label, duration):
    if not isinstance(items, list):
        raise ValueError(f'{label} must be a list')
    found, ends = {}, {}
    for item in items:
        if not isinstance(item, dict):
            raise ValueError(f'{label} entries must be objects')
        identity = item.get('id')
        if not isinstance(identity, str) or not identity or identity in found:
            raise ValueError(f'{label} requires nonempty unique IDs')
        start = finite(item.get('start'), f'{label} start', 0)
        end = finite(item.get('end'), f'{label} end', 0)
        if not start < end <= duration:
            raise ValueError(f'{label} interval must fit audio and have positive length')
        track = item.get('track', 'main')
        if not isinstance(track, str) or not track:
            raise ValueError(f'{label} track must be a nonempty string')
        if start < ends.get(track, 0):
            raise ValueError(f'{label} intervals overlap or are unordered within track {track}')
        ends[track] = end
        if label in ('words', 'phrases'):
            if not isinstance(item.get('text'), str) or not item['text'].strip():
                raise ValueError(f'{label} requires nonempty text')
            if 'reviewed' in item and not isinstance(item['reviewed'], bool):
                raise ValueError(f'{label} reviewed must be boolean')
        found[identity] = item
    return found


def compile_document(root, data):
    if (not isinstance(data, dict) or isinstance(data.get('schema_version'), bool)
            or data.get('schema_version') != 1):
        raise ValueError('Expected a sync.json object with schema_version 1')
    try:
        fps = Fraction(str(data['fps']))
    except (KeyError, ValueError, ZeroDivisionError) as exc:
        raise ValueError('fps must be a positive number or rational string') from exc
    if not 1 <= fps <= 240:
        raise ValueError('fps must be between 1 and 240')
    audio = data.get('audio')
    if not isinstance(audio, dict) or not isinstance(audio.get('path'), str):
        raise ValueError('audio requires a local path, sha256, and measured duration')
    duration = finite(audio.get('duration'), 'audio duration', 0)
    if duration == 0:
        raise ValueError('audio duration must be positive')
    path = local_path(root, audio['path'])
    if not path.is_file() or fingerprint(path) != audio.get('sha256'):
        raise ValueError('Audio missing or SHA-256 changed: recheck alignment before compiling')
    sections = intervals(data.get('sections', []), 'sections', duration)
    words = intervals(data.get('words', []), 'words', duration)
    phrases = intervals(data.get('phrases', []), 'phrases', duration)
    beats = data.get('beats', [])
    if not isinstance(beats, list):
        raise ValueError('beats must be a list')
    previous = -1.0
    for time in beats:
        current = finite(time, 'beat time', 0)
        if current <= previous or current >= duration:
            raise ValueError('Beats must be strictly increasing and inside audio')
        previous = current
    cues = data.get('cues', [])
    if not isinstance(cues, list):
        raise ValueError('cues must be a list')
    compiled, cue_ids = [], set()
    for cue in cues:
        if not isinstance(cue, dict):
            raise ValueError('Cue must be an object')
        identity = cue.get('id')
        if not isinstance(identity, str) or not identity or identity in cue_ids:
            raise ValueError('Cues require nonempty unique IDs')
        cue_ids.add(identity)
        kind = cue.get('kind')
        if kind not in ('lyric', 'accent', 'scene', 'ambient'):
            raise ValueError('Unknown cue kind')
        anchor = cue.get('anchor')
        if not isinstance(anchor, dict) or len(anchor) != 1:
            raise ValueError('Each cue needs exactly one anchor')
        key, value = next(iter(anchor.items()))
        target = None
        if key == 'time':
            base = finite(value, 'anchor time', 0)
            if base >= duration:
                raise ValueError('Anchor time is outside audio')
        elif key == 'beat_index':
            if isinstance(value, bool) or not isinstance(value, int) or not 0 <= value < len(beats):
                raise ValueError('Invalid zero-based beat_index')
            base = beats[value]
        elif key in ('word_id', 'phrase_id', 'section_id'):
            index = {'word_id': words, 'phrase_id': phrases, 'section_id': sections}[key]
            if not isinstance(value, str) or value not in index:
                raise ValueError(f'Unknown {key}')
            target = index[value]
            base = target['start']
        else:
            raise ValueError('Unknown cue anchor type')
        if kind == 'lyric' and (key not in ('word_id', 'phrase_id') or target.get('reviewed') is not True):
            raise ValueError('Lyric cues require reviewed word or phrase timing')
        offset = finite(cue.get('offset', 0), 'cue offset')
        length = finite(cue.get('duration'), 'cue duration', 0)
        start, end = base + offset, base + offset + length
        if length == 0 or start < 0 or end > duration:
            raise ValueError('Cue must have positive duration and fit audio')
        first, last = frame_at(start, fps), frame_at(end, fps)
        if first == last:
            raise ValueError('Cue collapses below one frame at selected fps')
        compiled.append({'id': identity, 'kind': kind, 'anchor': anchor,
                         'anchor_seconds': base, 'raw_start_seconds': start,
                         'raw_end_seconds': end, 'start_frame': first, 'end_frame': last,
                         'start_seconds': float(first / fps), 'end_seconds': float(last / fps),
                         'duration_frames': last - first,
                         'quantization_error_ms': (float(first / fps) - start) * 1000})
    compiled.sort(key=lambda cue: (cue['start_frame'], cue['id']))
    observations = data.get('observations', [])
    if not isinstance(observations, list):
        raise ValueError('observations must be a list')
    by_id = {cue['id']: cue for cue in compiled}
    checks, observed_ids = [], set()
    for item in observations:
        if not isinstance(item, dict):
            raise ValueError('Observation must be an object')
        identity = item.get('cue_id')
        if not isinstance(identity, str) or identity not in by_id or identity in observed_ids:
            raise ValueError('Observation needs a known unique cue_id')
        observed_ids.add(identity)
        observed = finite(item.get('observed_time'), 'observed_time', 0)
        if observed > duration:
            raise ValueError('Observation is outside audio')
        cue = by_id[identity]
        error = observed - cue['raw_start_seconds']
        tolerance = finite(item.get('tolerance_frames', 2 if cue['kind'] == 'lyric' else 1),
                           'tolerance_frames', 0)
        checks.append({'cue_id': identity, 'error_ms': error * 1000,
                       'error_frames': error * float(fps), 'tolerance_frames': tolerance,
                       'within_tolerance': abs(error) * float(fps) <= tolerance + 1e-9})
    phrase_list = sorted(phrases.values(), key=lambda item: (item['start'], item['id']))
    captions, warning = [], []
    tracks = {phrase.get('track', 'main') for phrase in phrase_list}
    if len(tracks) > 1:
        warning.append('Multiple phrase tracks: SRT excludes them; author separate caption tracks explicitly.')
    for phrase in phrase_list:
        if phrase.get('reviewed') is not True:
            warning.append(f'Unreviewed phrase excluded from SRT: {phrase["id"]}')
        elif len(tracks) <= 1:
            if timestamp(phrase['start']) == timestamp(phrase['end']):
                raise ValueError('Phrase collapses below SRT millisecond precision')
            text = phrase['text'].strip()
            if '\n\n' in text.replace('\r\n', '\n'):
                raise ValueError('Caption text cannot contain blank separator lines')
            captions.append(f'{len(captions) + 1}\n{timestamp(phrase["start"])} --> '
                            f'{timestamp(phrase["end"])}\n{text}\n')
    if not captions:
        warning.append('No reviewed single-track phrase captions; SRT is empty.')
    status = ('unverified' if not observations else
              'complete' if len(observed_ids) == len(compiled) else 'partial')
    report = {'schema_version': 1, 'fps': str(fps), 'audio': audio,
              'duration_frames': math.ceil(Fraction(str(duration)) * fps),
              'cues': compiled, 'warnings': warning,
              'export_timing_review': {'coverage': status, 'observations': checks,
                                        'out_of_tolerance': sum(not check['within_tolerance'] for check in checks)}}
    return report, '\n'.join(captions)


def compile_file(root):
    source = local_path(root, 'sync.json')
    with source.open(encoding='utf-8') as input_file:
        data = json.load(input_file)
    report, captions = compile_document(root, data)
    timeline = output_path(root, 'analysis/timeline.json')
    srt = output_path(root, 'captions.srt')
    # All content validates before either existing output is replaced.
    atomic_json(timeline, report)
    atomic_text(srt, captions)
    return report, timeline


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--video-dir', required=True, type=Path)
    args = parser.parse_args()
    try:
        report, output = compile_file(video_root(args.video_dir))
    except (OSError, ValueError, KeyError, TypeError) as exc:
        parser.exit(1, f'Sync compilation failed: {exc}\n')
    print(json.dumps({'output': str(output), 'cue_count': len(report['cues']),
                      'export_timing_review': report['export_timing_review'],
                      'warnings': report['warnings']}))
    return 2 if report['export_timing_review']['out_of_tolerance'] else 0


if __name__ == '__main__':
    raise SystemExit(main())
