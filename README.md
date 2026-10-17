# Devotional Song Studio

A repository skill for original devotional storytelling rap and songs in Hindi or another requested language. Generate audio with ElevenLabs Music or https://gemini.google.com (Brave/Playwright for Gemini); generate images with Gemini or ChatGPT web; author synchronized HyperFrames motion graphics in your chosen AI code editor.

The workflow analyzes supplied song references, develops an original story and refrain, generates/reviews audio takes, plans beat/vocal/story cues, and prepares video and YouTube release assets. Uploading or publishing follows the user's specific authorization.

## Use the skill

The entry point is [skills/devotional-song-studio/SKILL.md](skills/devotional-song-studio/SKILL.md). Reference that file directly in Codex, or copy the `devotional-song-studio` folder into your Codex skills directory to make `$devotional-song-studio` discoverable. Existing skill installations should be reviewed before replacement.

For another AI code editor, open this repository and tell its agent to read the same SKILL.md and studio-preferences.md first, then the relevant references. The editor needs local file/terminal access, Python and browser automation for Gemini, and Node/HyperFrames for motion work. Skill discovery syntax varies by editor; the Markdown instructions and editable project files are portable. These instructions do not establish that every editor has been integration-tested. Use [editor handoff](skills/devotional-song-studio/references/editor-handoff.md) to recover missing HyperFrames instructions and preserve the project's resume point.

Example request:

> Use $devotional-song-studio. Create an original Hindi devotional storytelling rap about Hanuman, using these references for cadence and narrative energy. Use my Brave/Gemini session for audio, then make a synchronized music video. Prepare the YouTube package; do not upload yet.

Supply reference songs and the subject/tradition. The skill asks only for missing essential decisions and preserves narrower requests such as lyrics only.

## Every video has its own folder

Before any video work:

```bash
python3 skills/devotional-song-studio/scripts/init_video.py \
  --song-slug hanuman-story --video-slug main-video
```

This creates `productions/hanuman-story/videos/main-video/` with local `audio/`, `assets/`, `analysis/`, `project/`, `previews/`, `exports/`, and `release/` directories. Re-running it preserves existing work. Browser authentication profiles stay outside production deliverables.

## Audio and timing tools

Requirements: Python 3.10+, FFmpeg/ffprobe for audio analysis. Browser execution also requires Brave and Python Playwright. Optional beat estimation requires compatible installed librosa and NumPy; no scientific packages are needed for basic envelope analysis or cue compilation. The tools do not install dependencies automatically.

1. Copy the selected take into the video's `audio/` folder.
2. Measure it:

   ```bash
   python3 skills/devotional-song-studio/scripts/analyze_audio.py \
     --video-dir productions/hanuman-story/videos/main-video \
     --input audio/master.mp3 --loudness
   ```

3. Review beat estimates, actual-sung text, word/phrase timings, and section boundaries. Author `sync.json` using [the documented format](skills/devotional-song-studio/references/rap-sync.md). Optional `--beats` requests librosa estimates; the output states explicitly when that dependency is unavailable.
4. Compile reviewed timing:

   ```bash
   python3 skills/devotional-song-studio/scripts/compile_sync.py \
     --video-dir productions/hanuman-story/videos/main-video
   ```

The result is `analysis/timeline.json` plus reviewed phrase captions in `captions.srt`. The compiler checks source SHA-256, time bounds, review status, anchors, and frame quantization. It keeps off-beat rap cues on the voice rather than snapping everything to a beat. It validates declared measured duration; it does not recognize lyrics or measure duration itself.

Cue compilation exits 0 on success, 1 on invalid input/execution failure, or 2 when supplied export observations exceed tolerance. Export review remains unverified until actual observations are supplied. These are intermediate formats; the installed HyperFrames workflow owns its own composition and `audiomap.json` contracts.

For production-sized audio the analyzer currently accepts measurable tracks up to 30 minutes; it is designed primarily for songs. It preserves source files and produces local analysis only. Loudness metrics are measurements, not an automatic normalization pass or a universal platform target.

## Motion design

The skill routes video work through the installed HyperFrames entry workflow. Its guidance covers section-specific choreography, selective punchline emphasis for dense rap, phrase-based lyrics, Devanagari shaping, deterministic feature-driven motion, and a short proof before a full build. See [motion direction](skills/devotional-song-studio/references/motion-direction.md) and [research](skills/devotional-song-studio/references/research.md).

Gemini model labels, feature availability, quotas, and output controls must be inspected in the account. The historical label “Argon” is unverified and is not required for new productions; inspect a named model only when the current request explicitly requires it. No automated Gemini generation or live rendering is claimed by installing this skill.

## Validate

```bash
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover \
  -s skills/devotional-song-studio/tests -v
```

The tests cover timing validation, fractional frame rates, stale audio, caption confidence, export observation errors, output preservation, folder isolation, and synthetic-audio analysis. The FFmpeg test skips when the binaries are missing. A skipped check is not evidence that its behavior passed.

See [QUALITY.md](QUALITY.md) for the current verified scope and remaining production checks. A real song, pronunciation review, rendered video, and live browser test are still required before making an end-to-end quality claim.
# devotional-song-studio
