# Rap, song, and animation synchronization

Read [research.md](research.md) for sources and limitations. The scripts implement this skill's timing contract, not HyperFrames' `audiomap.json` format; adapt to the installed music-to-video workflow without renaming incompatible data.

## Establish the audio clock

Create the video's folder first. Copy the selected reviewed take into `audio/`, fingerprint it, and retain the unmodified song master. Decode without deleting silence or normalizing playback speed. Use seconds from the start of this exact media as the canonical clock. File duration and decoded duration can differ slightly for compressed audio; use the decoded playback timeline and check the exported result.

Run the feature helper with resolved skill/video paths:

```bash
python3 <skill>/scripts/analyze_audio.py --video-dir <video-folder> --input audio/master.mp3
```

This uses FFmpeg and Python's standard library to produce `analysis/audio-analysis.json`: audio identity, decoded duration, RMS envelope, and positive energy-change candidates. These candidates are not verified beats or vocal timestamps. Optional `--beats` uses installed librosa/NumPy; if unavailable, the report explicitly says beat estimation was not run. Prefer the owning music-to-video workflow's analyzer when it already supplies adequate features. Use `--loudness` for a read-only FFmpeg measurement pass; it does not change the source audio.

## Review three layers

1. **Musical structure:** listen for pulse, first downbeat, bars, pickups, half/double-time ambiguities, sparse intros, tempo changes, and verse/hook/bridge/outro boundaries. Inspect estimated beats at beginning, middle, and end. A loud transient is not necessarily a beat; every fourth detected beat is not a verified downbeat. Preserve local beat times for variable tempo rather than projecting a single BPM forever.
2. **Vocal structure:** transcribe what is actually performed, then correct the text before alignment. Use an alignment model suitable for that language. Hindi must not silently go through an English/European-only recognizer. Mark missing words, uncertain boundaries, ad-libs, overlapping voices, and sustained syllables. A separated vocal can help alignment, but check it shares the master's duration/origin; apply measured offsets back to the master. It is an analysis derivative, not an automatic replacement soundtrack.
3. **Narrative structure:** mark revelation, a consequential choice, prayer, and resolution. Choose scene cuts for musical phrases and meaning; let an off-beat rap punchline land with the voice rather than snapping it to a kick.

Align repeated hooks separately; do not copy the first hook's timestamps to later performances. For code-switching, review language spans separately and preserve original script. If word timing cannot be verified, use phrase-level text and keep its uncertainty explicit. Never manufacture word timestamps by evenly dividing a line's duration.

## Author `sync.json`

Store at the video root. `audio.path` is relative to that root, `sha256` is the actual source fingerprint, and `duration` is measured seconds. Set `fps` to the project rate, e.g. `"30"` or `"30000/1001"`. The following is a compact structural example, not actual song analysis:

```json
{
  "schema_version": 1,
  "fps": "30",
  "audio": {"path": "audio/master.wav", "sha256": "<measured SHA-256>", "duration": 12.0},
  "beats": [0.5, 1.0, 1.5, 2.0],
  "sections": [{"id": "verse-1", "start": 0.0, "end": 12.0}],
  "words": [{"id": "w1", "text": "मन", "start": 1.08, "end": 1.42, "reviewed": true}],
  "phrases": [{"id": "p1", "text": "मन", "start": 1.08, "end": 1.42, "reviewed": true}],
  "cues": [
    {"id": "accent-1", "kind": "accent", "anchor": {"beat_index": 2}, "offset": 0.0, "duration": 0.2},
    {"id": "word-1", "kind": "lyric", "anchor": {"word_id": "w1"}, "offset": 0.0, "duration": 0.34}
  ]
}
```

`beat_index` is zero-based. Each anchor contains exactly one of `time`, `beat_index`, `word_id`, `phrase_id`, or `section_id`. Word/phrase/section anchors use their start. Cue kinds are `lyric`, `accent`, `scene`, or `ambient`. Every cue has a positive duration. Lyric cues require reviewed word/phrase anchors; use ambient or scene cues for non-lyric design. Separate simultaneous voices into explicit tracks; within each word/phrase track, timestamps must be ordered and nonoverlapping. `track` defaults to `main`.

Compile after manual timing review:

```bash
python3 <skill>/scripts/compile_sync.py --video-dir <video-folder>
```

It verifies file identity, time ranges, anchors, and cue IDs, then creates `analysis/timeline.json` and `captions.srt`. It never changes `sync.json`. Captions come only from reviewed phrases. Word highlights can use reviewed word cues while phrase captions remain readable. Missing phrase review produces a warning, not fabricated captions.

The compiler validates the declared measured duration; use the analyzer's decoded duration rather than guessing. It does not re-transcribe or independently measure the audio. Exit status 2 means supplied export observations exceeded their timing tolerance; the written report identifies those cues. Exit status 1 means invalid input or execution failure. Exit status 0 means compilation succeeded, with review coverage still stated explicitly.

## Schedule motion without drift

Use `analysis/timeline.json` as a cue list. Numeric timeline positions are absolute seconds; translate to local scene time by subtracting that scene's absolute start. For a requested arrival at a cue, start anticipation before it and put the visual landing/peak on it; do not confuse tween start with landing. Store both if the choreography uses them. Core/registry/animation skills own the render implementation.

The compiler rounds each absolute cue time independently to the nearest frame and computes end frames from absolute endpoints. It does not add rounded beat intervals repeatedly. Preserve raw source timestamps alongside frame times. The animation's visual event must be scheduled at `start_seconds`, not accidentally at `start_seconds + duration`.

Keep primary lyrics stable/readable while highlighting selected words. Use phrase holds for dense double-time rap; selective rhyme or punchline emphasis is more legible than animated subtitles on every syllable. Draw sustained-note highlights over the held word without splitting Indic syllables.

## Check the exported video

Listen/view local windows around intro, a fast verse, refrain, bridge, and final line; also check the longest section for accumulating drift. Project settings may target an accent landing within one frame and reviewed lyric emphasis within two frames. These are adjustable studio goals, not a universal perceptual standard or proof of actual alignment.

For measured verification, add `observations` to `sync.json`: `{"cue_id":"accent-1","observed_time":1.5333}`. These must be visually/audibly inspected export timestamps, not copies of intended values. The compiler reports signed error in milliseconds/frames for each observation. It reports `unverified` when none exist and `partial` until all cues have observations. It cannot detect whether a supplied observation is truthful. Review cues beyond tolerance and inspect causes before applying any global offset. Constant offset, gradual drift, and one misaligned word need different fixes.

Changing the audio hash makes existing alignment stale. Changing fps requires recompilation and another rendered timing check. Never repair animation sync by stretching the final song without explicit creative direction.
