# Research behind the timing and quality workflow

Reviewed 2026-10-17. These sources support specific mechanics; they do not certify the skill's artistic quality. The studio practices in the other references are design choices derived from these constraints.

| Primary source | Finding | Implementation decision |
| --- | --- | --- |
| [librosa beat tracker](https://librosa.org/doc/0.11.0/generated/librosa.beat.beat_track.html) | Beat tracking combines onset strength, tempo estimation, and beat selection; it can return no beats for insufficient onset evidence | Keep beats estimated until reviewed; do not equate RMS peaks with downbeats; record method/version |
| [librosa onset detection](https://librosa.org/doc/0.11.0/generated/librosa.onset.onset_detect.html) | Onsets and beats are different analysis outputs | Label the lightweight helper's energy-change candidates honestly; use a real beat estimator when needed |
| [WhisperX repository](https://github.com/m-bain/whisperX) | Alignment uses language-specific models; overlapping speech and out-of-dictionary tokens remain limitations | Correct actual-sung text, track review per segment, handle code-switches and uncertainty |
| [Improving Lyrics Alignment through Joint Pitch Detection](https://arxiv.org/abs/2202.01646) | Singing alignment can benefit from musical information and line-boundary handling | Treat speech alignment as a draft; check sustained notes, repeated lines, and line boundaries against the song |
| [W3C Devanagari layout requirements](https://www.w3.org/International/ilreq/devanagari/) | Orthographic syllables and conjuncts require shaping-aware handling | Animate whole words/phrases by default and test final-size typography |
| [GSAP timeline](https://www.gsap.com/docs/v3/GSAP/gsap.timeline%28%29/) | Timelines accept numeric positions in absolute seconds | Compile all cues from the same audio clock and convert scene-local positions explicitly |
| [FFmpeg loudnorm](https://ffmpeg.org/ffmpeg-filters.html#loudnorm) | Loudness analysis includes integrated loudness, range, and true peak; normalization can operate in linear or dynamic modes | Measure before processing, preserve source, do not assert a universal platform loudness target |

Local HyperFrames contracts were also inspected: entry routing, music-to-video route, core composition rules, animation rules, CLI, and media-use transcription. The owning music-to-video route expects `audiomap.json`; this skill's `sync.json` and `analysis/timeline.json` are separate, documented intermediate artifacts. Read the installed workflow's current format when adapting them. Do not claim compatibility from a filename alone.

## What remains empirical

Beat estimates, recognition accuracy, and pronunciation vary with a track and language. One synthetic click test cannot validate a devotional vocal. Frame budgets in this skill are adjustable studio checks. An end-to-end quality claim still requires a real reference-driven song, corrected sung transcript, inspected export, and listening/viewing feedback.
