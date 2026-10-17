# Production state, folders, and revisions

## Ownership

Song writing and provider take files belong under `productions/<song-slug>/`. Before doing anything for a video, create `videos/<video-slug>/` there. For a standalone video without a song production, use `productions/<project-slug>/videos/<video-slug>/` with the same rule. This is the user's explicit folder preference.

```text
productions/<song-slug>/
  production.json
  reference-analysis.md
  story.md
  lyrics.md
  generation-prompt.md
  pronunciation.md          # when pronunciation work is needed
  mix-review.md             # when processing/finishing is performed
  audio/take-01/
  audio-review.md
  videos/<video-slug>/
    video.json
    BRIEF.md
    storyboard.md
    motion.md
    transcript.md
    captions.srt
    beat-map.json
    audio/
    assets/
    analysis/
    project/
    previews/
    exports/
    release/
```

Create folders before use; do not populate empty placeholder documents and call them complete. `scripts/init_video.py --song-slug <song> --video-slug <video>` creates the video directories and initial `video.json` without overwriting existing work. Its default workspace is the current directory. Run it from the workspace root or pass `--workspace` explicitly.

Keep every video-specific command's working directory and output path inside this video folder. Install/scaffold HyperFrames in `project/`, not the workspace root. Local dependencies may remain in `project/`; reusable tool caches can stay in their normal external locations. Copy the selected source audio into the video's `audio/` folder for portability, preserving the song's original take. Keep browser authentication profiles outside all production folders. No media should depend on a transient signed download URL.

Save the HyperFrames workflow's brief at the location it requires inside `project/`; the video-level `BRIEF.md` can link to that canonical file instead of duplicating its contents. Resolve other framework-required state the same way. A requested alternate crop/export of the same video may stay in its folder; a separately developed video gets a sibling folder. Follow a user-specified location when supplied, retaining the one-folder-per-video rule.

## Evidence for stage completion

| Stage | Minimum evidence | When missing |
| --- | --- | --- |
| Brief ready | Subject, language, requested scope and usable inputs or explicit limitations | Ask only for essential missing decisions |
| Lyrics ready | Original lyrics, story/arrangement, pronunciation notes, recorded revision findings | Revise before submitting audio |
| Audio requested | Saved prompt/settings and attempt state | Do not count unsent drafts as submissions |
| Audio available | Observed result, local nonempty decodable file | Inspect pending result before any new submission |
| Audio selected | Actual-audio review and selected source path/fingerprint | Label provisional when listening is unavailable |
| Video planned | Dedicated folder, audio identity, transcript confidence, storyboard and assets plan | Continue independent visual planning without inventing timing |
| Video rendered | Real export, stream/duration checks, representative visual/audio review | Keep rendered-but-unreviewed status explicit |
| Release ready | Final file identity, metadata, captions and unresolved settings | Finish reviewable materials before asking about release |
| Uploaded/published | Observed platform status, ID/URL and actual visibility | Treat uncertain submission as pending, inspect before retry |

Use these as evidence requirements, not a rigid order that blocks useful independent work. Keep operation state (`planned`, `submitted`, `pending`, `completed`, `failed`, `unknown`) distinct from creative readiness. A timeout is not a failed generation. Write state atomically via a temporary file and replace when implementing helpers that mutate production records.

## Audio identity and revisions

Record selected source relative path, SHA-256, duration, and take ID in the video's `video.json`. Record the copied audio path and verify its hash matches. Mark timing review pending until the actual transcript is checked. A file hash identifies bytes, not artistic quality or rights.

If selected audio changes, keep the prior version, update the selected identity, and mark transcript timing, beat map, scene timing, captions, and renders stale. Recheck each dependency before reusing it. Lyric-only revisions do not rewrite what an existing take actually sings. Video-only visual changes do not require regenerating audio.

For rap-synchronized video, also keep `sync.json` at the video root and generated analysis/timeline files in `analysis/`. The sync compiler rejects a source-file fingerprint mismatch. Its timing-review coverage describes supplied export observations; it cannot substitute for actually listening/viewing the export.

## Preferences and learning

Read `studio-preferences.md` at workspace root if it exists. Record only clearly expressed durable preferences there: preferred script, narration/vocal traits, visual depiction preferences, channel conventions. Record a production-specific choice in that production. Preserve the user's language choices; do not assume devotional means only Hindu subjects or all languages can be assessed equally well.

After real feedback, save the issue, evidence, and specific next adjustment in the production record. Generalize to the skill only when repeated outcomes justify it. Do not add a universal restriction after one disliked take.
