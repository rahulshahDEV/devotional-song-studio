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

## Vocal realism, ElevenLabs, and motion expansion

Checked 2026-10-17. These links establish product mechanics. Performance, mixing, arrangement, and motion recommendations in this skill are studio judgments to audition, not vendor promises.

| Official source | Finding used here |
| --- | --- |
| [Eleven Music product guide](https://elevenlabs.io/docs/eleven-creative/products/music) | Vocal music and section editing are distinct from speech synthesis; documented rap capability still needs a language-specific audition |
| [Music prompting](https://elevenlabs.io/docs/overview/capabilities/music/best-practices) | Concrete musical/production direction and ordered arrangements offer more useful control than generic quality words |
| [Music API quickstart](https://elevenlabs.io/docs/eleven-api/guides/cookbooks/music) | Prompt and composition-plan routes; save exact inputs and use the current SDK/schema |
| [TTS best practices](https://elevenlabs.io/docs/overview/capabilities/text-to-speech/best-practices) | Delivery and pronunciation controls vary by model; do not transplant recipes across products |
| [Voice changer](https://elevenlabs.io/docs/overview/capabilities/voice-changer) | Conversion is driven by existing delivery; audition musical material rather than guaranteeing song suitability |
| [Music stem separation](https://elevenlabs.io/docs/api-reference/music/separate-stems) | Service separation exists; derived material needs artifact and alignment checks |
| [Forced alignment](https://elevenlabs.io/docs/api-reference/forced-alignment/create/) | Audio plus supplied text produces timing; transcript correctness and singing review remain separate |
| [HyperFrames core](https://github.com/heygen-com/hyperframes/blob/main/packages/core/docs/core.md) | Framework owns media timing; follow the installed contract for clips and registered timelines |
| [HeyGen rendering explanation](https://www.heygen.com/research/html-to-video) | Independent frame seeking requires animation state reproducible at arbitrary timestamps |
| [FFmpeg filters](https://ffmpeg.org/ffmpeg-filters.html#loudnorm) | Measured loudness processing supports a reproducible finishing pass; measurements alone do not judge a performance |

Implementation details live in [audio-production.md](audio-production.md), [elevenlabs.md](elevenlabs.md), and [motion.md](motion.md). Model labels, plan fields, export formats, account access, pricing, and UI controls should be verified at execution. No credits were used, live ElevenLabs calls made, song listened to, or video rendered for this documentation expansion.

## Editor dependency recovery

Checked 2026-10-17: the [official HyperFrames skills guide](https://github.com/heygen-com/hyperframes/blob/main/docs/guides/skills.mdx) documents standalone core freshness/install commands and editor discovery. Its [plugin installation contract](https://github.com/heygen-com/hyperframes/blob/main/skills/hyperframes/references/plugin-installation.md) assigns bundled skills and updates to the plugin manager. [editor-handoff.md](editor-handoff.md) preserves that distinction; neither path certifies every AI editor or authorizes overriding environment execution permissions.
