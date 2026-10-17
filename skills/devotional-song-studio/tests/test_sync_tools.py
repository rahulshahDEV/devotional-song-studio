"""Local regression checks; synthetic audio is not a real-song quality evaluation."""

import argparse
from copy import deepcopy
from fractions import Fraction
import json
import math
from pathlib import Path
import shutil
import struct
import subprocess
import sys
import tempfile
import unittest
import wave

SCRIPTS = Path(__file__).resolve().parents[1] / 'scripts'
sys.path.insert(0, str(SCRIPTS))
from analyze_audio import analyze, features
from compile_sync import compile_document, compile_file, frame_at
from init_video import initialize
from sync_common import fingerprint, output_path


class SyncToolsTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix='devotional-sync-')
        self.addCleanup(self.temp.cleanup)
        self.root = initialize(Path(self.temp.name), 'test-song', 'test-video')
        self.audio = self.root / 'audio/master.wav'
        self.rate = 22050
        self.hits = [0.5, 1.0, 1.5, 2.0]
        values = []
        for index in range(self.rate * 4):
            time = index / self.rate
            amplitude = 0.0
            for hit in self.hits:
                elapsed = time - hit
                if 0 <= elapsed < 0.03:
                    amplitude += 0.7 * math.exp(-elapsed * 80) * math.sin(2 * math.pi * 900 * elapsed)
            values.append(max(-32768, min(32767, round(amplitude * 32767))))
        with wave.open(str(self.audio), 'wb') as output:
            output.setparams((1, 2, self.rate, 0, 'NONE', 'not compressed'))
            output.writeframes(struct.pack('<' + 'h' * len(values), *values))
        self.data = {
            'schema_version': 1, 'fps': '30',
            'audio': {'path': 'audio/master.wav', 'sha256': fingerprint(self.audio), 'duration': 4.0},
            'beats': self.hits,
            'sections': [{'id': 'verse', 'start': 0, 'end': 4}],
            'words': [{'id': 'w1', 'text': 'मन', 'start': 1.08, 'end': 1.42, 'reviewed': True}],
            'phrases': [{'id': 'p1', 'text': 'मन', 'start': 1.08, 'end': 1.42, 'reviewed': True}],
            'cues': [
                {'id': 'beat', 'kind': 'accent', 'anchor': {'beat_index': 2}, 'duration': 0.2},
                {'id': 'word', 'kind': 'lyric', 'anchor': {'word_id': 'w1'}, 'duration': 0.34}
            ]
        }

    def test_compiles_offbeat_word_without_snapping_to_beat(self):
        report, srt = compile_document(self.root, self.data)
        cue = next(item for item in report['cues'] if item['id'] == 'word')
        self.assertEqual(cue['anchor_seconds'], 1.08)
        self.assertEqual(cue['start_frame'], 32)
        self.assertIn('00:00:01,080 --> 00:00:01,420\nमन', srt)
        self.assertEqual(report['export_timing_review']['coverage'], 'unverified')

    def test_rational_fps_and_no_cumulative_interval_rounding(self):
        fps = Fraction('30000/1001')
        for index in range(1, 500):
            time = index * 60 / 137
            self.assertLessEqual(abs(float(frame_at(time, fps) / fps) - time), float(1 / fps) / 2 + 1e-10)
        data = deepcopy(self.data)
        data['fps'] = '30000/1001'
        report, _ = compile_document(self.root, data)
        self.assertEqual(report['fps'], '30000/1001')

    def test_changed_audio_rejects_stale_alignment(self):
        self.audio.write_bytes(self.audio.read_bytes() + b'changed')
        with self.assertRaisesRegex(ValueError, 'SHA-256'):
            compile_document(self.root, self.data)

    def test_unreviewed_word_cannot_drive_lyric_cue(self):
        self.data['words'][0]['reviewed'] = False
        with self.assertRaisesRegex(ValueError, 'reviewed'):
            compile_document(self.root, self.data)

    def test_unreviewed_phrase_excluded_from_captions(self):
        self.data['phrases'][0]['reviewed'] = False
        report, srt = compile_document(self.root, self.data)
        self.assertEqual(srt, '')
        self.assertTrue(any('Unreviewed phrase' in item for item in report['warnings']))

    def test_multiple_voices_not_silently_flattened_into_srt(self):
        self.data['phrases'].append({'id': 'p2', 'text': 'जय', 'start': 1.1, 'end': 1.5,
                                      'reviewed': True, 'track': 'response'})
        report, srt = compile_document(self.root, self.data)
        self.assertEqual(srt, '')
        self.assertTrue(any('Multiple phrase tracks' in item for item in report['warnings']))

    def test_invalid_timing_cases(self):
        edits = [
            lambda data: data.update(fps='0'),
            lambda data: data.update(fps='NaN'),
            lambda data: data.update(beats=[1, 0.5]),
            lambda data: data.update(beats=[True]),
            lambda data: data['words'][0].update(start=float('nan')),
            lambda data: data['words'].append(dict(data['words'][0])),
            lambda data: data['cues'][0].update(anchor={'beat_index': -1}),
            lambda data: data['cues'][0].update(anchor={'time': 0, 'beat_index': 0}),
            lambda data: data['cues'][0].update(duration=0.001),
            lambda data: data['cues'][0].update(offset=-3),
            lambda data: data['cues'][0].update(duration=10),
            lambda data: data['audio'].update(path='../../outside.wav'),
        ]
        for edit in edits:
            with self.subTest(edit=edit):
                data = deepcopy(self.data)
                edit(data)
                with self.assertRaises(ValueError):
                    compile_document(self.root, data)

    def test_per_track_overlaps_are_rejected(self):
        self.data['words'].append({'id': 'w2', 'text': 'जय', 'start': 1.2, 'end': 1.5})
        with self.assertRaisesRegex(ValueError, 'overlap'):
            compile_document(self.root, self.data)

    def test_export_observations_report_signed_error_and_coverage(self):
        self.data['observations'] = [{'cue_id': 'word', 'observed_time': 1.28}]
        report, _ = compile_document(self.root, self.data)
        review = report['export_timing_review']
        self.assertEqual(review['coverage'], 'partial')
        self.assertEqual(review['out_of_tolerance'], 1)
        self.assertAlmostEqual(review['observations'][0]['error_ms'], 200)
        self.data['observations'].append({'cue_id': 'beat', 'observed_time': 1.5})
        report, _ = compile_document(self.root, self.data)
        self.assertEqual(report['export_timing_review']['coverage'], 'complete')
        self.assertEqual(report['export_timing_review']['out_of_tolerance'], 1)

    def test_invalid_inputs_preserve_existing_outputs(self):
        timeline = self.root / 'analysis/timeline.json'
        timeline.write_text('existing work')
        (self.root / 'captions.srt').write_text('existing captions')
        self.data['beats'] = [2, 1]
        (self.root / 'sync.json').write_text(json.dumps(self.data))
        with self.assertRaises(ValueError):
            compile_file(self.root)
        self.assertEqual(timeline.read_text(), 'existing work')
        self.assertEqual((self.root / 'captions.srt').read_text(), 'existing captions')

    def test_cli_writes_outputs_and_returns_failure_for_observed_sync_error(self):
        self.data['observations'] = [{'cue_id': 'beat', 'observed_time': 1.9}]
        (self.root / 'sync.json').write_text(json.dumps(self.data, ensure_ascii=False))
        result = subprocess.run([sys.executable, str(SCRIPTS / 'compile_sync.py'),
                                 '--video-dir', str(self.root)], capture_output=True, text=True)
        self.assertEqual(result.returncode, 2, result.stderr)
        self.assertTrue((self.root / 'analysis/timeline.json').is_file())
        self.assertIn('मन', (self.root / 'captions.srt').read_text())

    def test_resume_does_not_overwrite_video_manifest(self):
        manifest = self.root / 'video.json'
        manifest.write_text('{"stage":"reviewed"}')
        initialize(Path(self.temp.name), 'test-song', 'test-video')
        self.assertEqual(json.loads(manifest.read_text())['stage'], 'reviewed')
        with self.assertRaises(argparse.ArgumentTypeError):
            initialize(Path(self.temp.name), '../outside', 'video')

    def test_silence_has_no_energy_candidates(self):
        envelope, candidates = features([0.0] * 22050, 22050, 10)
        self.assertTrue(envelope)
        self.assertEqual(candidates, [])

    def test_symlinked_generated_output_cannot_overwrite_audio(self):
        before = fingerprint(self.audio)
        (self.root / 'captions.srt').symlink_to(self.audio)
        (self.root / 'sync.json').write_text(json.dumps(self.data))
        with self.assertRaisesRegex(ValueError, 'symlink'):
            compile_file(self.root)
        self.assertEqual(fingerprint(self.audio), before)
        self.assertFalse((self.root / 'analysis/timeline.json').exists())

    def test_symlinked_output_directory_is_rejected(self):
        (self.root / 'analysis').rmdir()
        (self.root / 'analysis').symlink_to(self.root / 'assets', target_is_directory=True)
        with self.assertRaisesRegex(ValueError, 'symlink'):
            output_path(self.root, 'analysis/timeline.json')

    @unittest.skipUnless(shutil.which('ffmpeg') and shutil.which('ffprobe'), 'FFmpeg required')
    def test_actual_ffmpeg_analysis_preserves_audio_and_finds_energy_events(self):
        before = fingerprint(self.audio)
        report, output = analyze(self.root, 'audio/master.wav', with_loudness=True)
        self.assertAlmostEqual(report['audio']['duration'], 4, places=4)
        self.assertEqual(fingerprint(self.audio), before)
        candidates = [item['time'] for item in report['energy_change_candidates']]
        for hit in self.hits:
            self.assertLess(min(abs(time - hit) for time in candidates), 0.025)
        self.assertEqual(report['beat_estimation']['status'], 'not_requested')
        self.assertEqual(report['loudness']['status'], 'measured')
        self.assertTrue(output.is_relative_to(self.root))


if __name__ == '__main__':
    unittest.main()
