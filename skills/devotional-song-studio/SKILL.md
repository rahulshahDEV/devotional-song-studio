---
name: devotional-song-studio
description: Create original devotional songs and storytelling rap in Hindi or another requested language using song references, Gemini music generation through Brave and Playwright, and an optional HyperFrames music video and YouTube release package. Use for a bhakti song production workflow, not general browser automation.
---

# Devotional Song Studio

Own the requested stages from reference analysis to a finished devotional song, optional video, and release package. Respect a narrower request such as lyrics only, a plan, or revising an existing take. Creating this skill does not authorize running generations or uploading content.

## Resume and scope

Use `productions/<song-slug>/` under the current workspace. Read its `production.json` and existing artifacts before starting. Store paths relative to that project. Keep private browser profiles outside production deliverables.

Keep `production.json` current with subject, language/script, audience, references and inspection status, stage, requested/observed model labels, actual UI duration options, submission budget, attempts, selected audio, artifact paths, unresolved issues, and upload authorization/status. Record unknowns honestly; a button click does not prove generation or publication succeeded.

Read [production-contract.md](references/production-contract.md) when creating/resuming a production, starting a video, or replacing selected audio. It defines stage evidence, folder ownership, revision rules, and preferences.

**Before any video work**, create a dedicated `productions/<song-slug>/videos/<video-slug>/` folder. All work specific to that video belongs inside it: brief, assets, selected audio copy, captions, HyperFrames project, previews, exports, and release package. Resume an existing video there; create a sibling folder for a separate video. Use the included `scripts/init_video.py` helper or create the same structure directly. Never scaffold a video's project or scatter its files in the workspace root.

Ask for missing essentials: subject/deity or tradition and references when the request depends on them. Bundle language, duration, vocal direction, and visual preferences only if needed. Default drafts to Hindi/Devanagari, a 2–3 minute target subject to generator capability, and devotional rap with a melodic refrain. These are editable creative defaults, not account capability claims.

## Write the song

Read [songwriting.md](references/songwriting.md) for analysis, story shapes, multilingual handling, and the generation prompt contract.

1. Inspect supplied material with available tools. Distinguish listening, transcript reading, and description-only analysis. If a link is inaccessible, use available information and state that limitation.
2. Save `reference-analysis.md`: useful craft traits and an original direction. Do not copy source lyrics, recognizable hooks, samples, or distinctive melody. Describe vocal traits instead of promising a named artist's voice.
3. Develop three concise concepts and recommend one. Unless the user asks to choose first, continue with the strongest fit and record the choice.
4. Save `story.md`, `lyrics.md`, and `generation-prompt.md`. Use natural spoken language, specific scenes, and a memorable refrain. Verify claims presented as scripture, label invented episodes, and avoid unintentional mixing of traditions.

Before generation, apply the lyric review in [quality-review.md](references/quality-review.md). Revise identified weaknesses rather than padding the brief with generic quality adjectives. A review is an internal work step, not an automatic request for user approval.

## Generate and select audio

Read [browser-gemini.md](references/browser-gemini.md) before connecting or submitting. Use Brave and Playwright/CDP at `gemini.google.com`. Do not substitute another generator, API, or account without the user's direction.

The requested label “Argon” is unverified. Record it verbatim and inspect visible model/tool labels. Public documentation names Lyria, but does not establish what this account exposes. Explain a mismatch; if the requested model is unavailable, finish independent writing and obtain the user's choice before generating with another model.

Default to at most three audio submissions per song unless the user sets another budget. Retries count. Reuse an in-progress result after a timeout instead of duplicating it. Do not buy credits or change subscription/activity settings as a side effect.

For every take save the exact prompt, visible model/settings, result status, and local download under `audio/take-01/`, etc. Review actual audio before choosing. Listen using available media tools; transcription and signal checks supplement listening. If listening is unavailable, mark the judgment provisional and make the take reviewable by the user. Converting MP3 to WAV does not restore quality.

Save `audio-review.md`: pronunciation of sacred names, actual words versus lyrics, story completeness, hook, vocal clarity, transitions, artifacts, and selection reasons. Preserve source files, provenance, and embedded watermarks. Do not promise exact lyric adherence or guaranteed commercial rights.

Use the audio review criteria in [quality-review.md](references/quality-review.md). Record why the selected take wins and what remains imperfect; an arbitrary numerical score is not proof of excellence.

## Create the video when requested

Read [video-release.md](references/video-release.md). Load the available `hyperframes` entry skill first and follow its current routing. A full song driven by its beat grid normally uses music-to-video; a custom narrative may use general-video. Use motion-graphics for short standalone animated units.

Lock the audio before detailed synchronization. Create a timed actual-sung transcript, section/beat map, visual treatment, and storyboard. Load HyperFrames core before composition HTML, registry before named effects, and media-use for sourced/generated assets. If an owning skill cannot be resolved, report the dependency instead of claiming a render.

Read [rap-sync.md](references/rap-sync.md) for the shared audio clock, beat/vocal/narrative timing layers, reviewed `sync.json`, and the audio-analysis/timing-compiler tools. Read [motion-direction.md](references/motion-direction.md) for section-specific choreography, shaping-safe Hindi typography, readable fast-rap treatment, and the short proof before a full build. See [research.md](references/research.md) for the primary sources and what remains empirical.

Measure and preserve the audio identity. Align lyrics to actual performed words, review uncertain timings, and compile animation cues from absolute timestamps. Keep intended timing separate from observations of the rendered export. Estimated beats or a successful compiler run do not establish synchronized final video.

Run all video commands from that video's `project/` directory as appropriate, resolve media paths locally, and keep generated artifacts within its parent video folder. Apply the visual and technical review in [quality-review.md](references/quality-review.md) before final rendering and delivery.

## Release and delivery

Prepare the reviewable release package in [video-release.md](references/video-release.md). Recheck current platform requirements for an upload. Follow explicit user authorization for the artifact, channel, visibility, and schedule. Reuse clear existing authorization; otherwise finish the package before requesting the missing decision. A preparation request does not authorize Publish.

Deliver artifact paths, concise quality findings, and outstanding limitations. Preserve completed work and the precise resume point on failure. Do not present a prompt, plan, or untested automation recipe as a finished song or uploaded video.
