#!/usr/bin/env python3
"""Measure local audio features; optionally estimate beats and loudness."""

import argparse
from array import array
import json
import math
from pathlib import Path
import re
import shutil
import subprocess
import sys

from sync_common import atomic_json, fingerprint, local_path, output_path, video_root


def features(samples, rate, hop_ms):
    hop = max(1, round(rate * hop_ms / 1000))
    envelope, changes, previous = [], [], 0.0
    for offset in range(0, len(samples), hop):
        chunk = samples[offset:offset + hop]
        rms = math.sqrt(sum(value * value for value in chunk) / len(chunk))
        center = (offset + len(chunk) / 2) / rate
        envelope.append({'time': round(center, 6), 'rms': round(rms, 8)})
        changes.append(max(0.0, rms - previous))
        previous = rms
    # Energy-change peaks are intentionally not labeled beat/onset ground truth.
    maximum = max(changes, default=0.0)
    candidates = []
    last_time = -1.0
    for index in range(1, len(changes) - 1):
        time = envelope[index]['time']
        if (maximum > 0 and changes[index] >= maximum * 0.2
                and changes[index] > changes[index - 1]
                and changes[index] >= changes[index + 1]
                and time - last_time >= 0.08):
            candidates.append({'time': time, 'strength': round(changes[index] / maximum, 6)})
            last_time = time
    return envelope, candidates


def analyze(root, input_path, hop_ms=10.0, with_beats=False, with_loudness=False):
    if not math.isfinite(hop_ms) or not 1 <= hop_ms <= 100:
        raise ValueError('hop-ms must be between 1 and 100')
    source = local_path(root, input_path)
    if not source.is_file():
        raise ValueError('Audio input does not exist')
    ffmpeg = shutil.which('ffmpeg')
    ffprobe = shutil.which('ffprobe')
    if not ffmpeg or not ffprobe:
        raise ValueError('Install FFmpeg/ffprobe before analyzing audio')
    metadata = subprocess.run([ffprobe, '-v', 'error', '-show_format', '-show_streams',
                               '-of', 'json', str(source)], capture_output=True,
                              text=True, check=True, timeout=30)
    info = json.loads(metadata.stdout)
    audio_streams = [stream for stream in info.get('streams', [])
                     if stream.get('codec_type') == 'audio']
    if not audio_streams:
        raise ValueError('Input has no audio stream')
    duration_hint = float(info.get('format', {}).get('duration', 0))
    if not math.isfinite(duration_hint) or duration_hint <= 0 or duration_hint > 1800:
        raise ValueError('Expected a measurable audio duration between 0 and 1800 seconds')
    rate = 22050
    decoded = subprocess.run([ffmpeg, '-v', 'error', '-nostdin', '-i', str(source),
                              '-map', '0:a:0', '-vn', '-ac', '1', '-ar', str(rate),
                              '-f', 'f32le', 'pipe:1'], capture_output=True,
                             check=True, timeout=120)
    samples = array('f')
    samples.frombytes(decoded.stdout)
    if sys.byteorder != 'little':
        samples.byteswap()
    if not samples or not all(math.isfinite(value) for value in samples):
        raise ValueError('Decoded audio is empty or contains non-finite samples')
    envelope, candidates = features(samples, rate, hop_ms)
    peak = max(abs(value) for value in samples)
    report = {
        'schema_version': 1,
        'audio': {'path': str(source.relative_to(root)), 'sha256': fingerprint(source),
                  'duration': len(samples) / rate, 'container_duration': duration_hint},
        'analysis': {'sample_rate': rate, 'hop_ms_requested': hop_ms,
                     'hop_samples': max(1, round(rate * hop_ms / 1000)),
                     'channels': 'mono analysis mix; original unchanged'},
        'sample_peak_dbfs_mono_analysis': 20 * math.log10(peak) if peak else None,
        'rms': envelope,
        'energy_change_candidates': candidates,
        'beats': [], 'beat_estimation': {'status': 'not_requested'},
        'loudness': {'status': 'not_requested'},
        'warnings': ['Energy changes are not verified beats or vocal timestamps.']
    }
    if with_beats:
        try:
            import librosa
            import numpy as np
        except ImportError:
            report['beat_estimation'] = {'status': 'unavailable',
                                          'reason': 'librosa and NumPy are required'}
        else:
            tempo, beats = librosa.beat.beat_track(
                y=np.asarray(samples, dtype=np.float32), sr=rate, units='time')
            report['beats'] = [float(time) for time in beats]
            tempos = np.asarray(tempo).reshape(-1).tolist()
            report['beat_estimation'] = {'status': 'estimated' if len(beats) else 'no_beats',
                                          'method': 'librosa.beat.beat_track',
                                          'version': librosa.__version__,
                                          'tempo_bpm': tempos, 'reviewed': False}
    if with_loudness:
        measured = subprocess.run(
            [ffmpeg, '-hide_banner', '-nostdin', '-i', str(source), '-map', '0:a:0',
             '-vn', '-af', 'loudnorm=print_format=json', '-f', 'null', '-'],
            capture_output=True, text=True, check=True, timeout=120)
        blocks = re.findall(r'\{[^{}]*"input_i"[^{}]*\}', measured.stderr)
        if not blocks:
            raise ValueError('FFmpeg returned no loudness measurement')
        values = json.loads(blocks[-1])
        measured_values = {}
        for key in ('input_i', 'input_tp', 'input_lra', 'input_thresh'):
            value = float(values[key])
            measured_values[key] = value if math.isfinite(value) else None
        report['loudness'] = {'status': 'measured', 'method': 'ffmpeg loudnorm analysis',
                              'values': measured_values,
                              'note': 'Input metrics only; no audio output or target mandate.'}
    output = output_path(root, 'analysis/audio-analysis.json')
    atomic_json(output, report)
    return report, output


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--video-dir', required=True, type=Path)
    parser.add_argument('--input', required=True, help='Absolute path or path relative to video folder')
    parser.add_argument('--hop-ms', type=float, default=10.0)
    parser.add_argument('--beats', action='store_true')
    parser.add_argument('--loudness', action='store_true')
    args = parser.parse_args()
    try:
        report, output = analyze(video_root(args.video_dir), args.input, args.hop_ms,
                                  args.beats, args.loudness)
    except (OSError, ValueError, KeyError, subprocess.SubprocessError) as exc:
        parser.exit(1, f'Audio analysis failed: {exc}\n')
    print(json.dumps({'output': str(output), 'duration': report['audio']['duration'],
                      'beat_estimation': report['beat_estimation']['status'],
                      'loudness': report['loudness']['status']}))


if __name__ == '__main__':
    main()
