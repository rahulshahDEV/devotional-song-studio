# Devotional Song Studio — production plan

One reusable skill lives at `skills/devotional-song-studio/SKILL.md`.
Use its file path directly; `$devotional-song-studio` becomes available if it is later installed into a discoverable skills directory. The workspace `.agents` directory is read-only in this session, so this is a local skill package rather than a global installation.

## Workflow

1. **Brief and references:** accept rap songs, audio, links, lyrics, or descriptions. Establish deity/tradition, language, story, audience, and duration. Default writing to Hindi/Devanagari. Analyze cadence, emotional progression, arrangement, and hook design; record what was actually heard or read.
2. **Original writing:** develop three concepts, choose the strongest fit, and write concrete scenes with an emotional turn, memorable refrain, and resolved ending. Produce lyrics and pronunciation notes. Distinguish verified scriptural episodes from imagined devotional stories.
3. **Gemini audio:** attach Playwright to Brave through a local debugging port and use the user's signed-in Gemini session. Inspect available music tools and models. Generate up to three takes by default, save exact prompts and downloads, and review actual audio before selection.
4. **Video:** lock the audio, transcribe what is actually sung, map sections and beats, and create the music video through HyperFrames. Use storytelling scenes, designed lyric typography, symbolic imagery, and purposeful animation. Export a YouTube master and requested Shorts versions.
5. **Release:** prepare titles, description, thumbnail brief, captions, credits, and settings. Upload/publish only within explicit user authorization for that artifact and channel. This skill-creation request does not authorize an upload.

## Quality improvement plan

1. **Make each video self-contained.** Before video research, asset generation, scaffolding, or editing, create `productions/<song-slug>/videos/<video-slug>/`. Put that video's brief, selected audio copy, assets, captions, project, previews, exports, and release package inside it. Resume an existing video in its existing folder. Browser login profiles stay outside deliverables.
2. **Improve the creative decisions.** Use a reference-to-originality matrix, compare hook candidates, write a causal story, and revise for natural diction, breath, specificity, and a changed final refrain. Preserve user preferences across songs without treating an individual reference as a permanent style rule.
3. **Make progress verifiable.** Define stage completion evidence, pending/unknown operation handling, selected-audio fingerprints, and downstream revision rules. Missing evidence remains unverified rather than becoming a fabricated success.
4. **Review quality before expensive work.** Review lyrics before generation, actual audio before detailed video work, and a storyboard/representative frames before the final render. Keep subjective craft assessment separate from technical pass/fail checks.
5. **Exercise realistic failures.** Review narrow-scope requests, inaccessible references, unsupported models, ambiguous submissions, changed audio, unfamiliar languages, multiple videos, and preparation-only uploads. Record local test results and live integration gaps.

No skill can honestly be certified the finest ever made. The practical target is excellent creative output, reliable execution, clear evidence, and improvement from real production feedback.

## Research and synchronization implementation

Primary sources reviewed: librosa beat/onset documentation, WhisperX, singing-alignment research, W3C Devanagari requirements, GSAP timelines, and FFmpeg loudness analysis. See `skills/devotional-song-studio/references/research.md` for links and design decisions.

Implemented audio-envelope/loudness analysis, optional librosa beat estimation, reviewed word/phrase/section cue contracts, absolute frame quantization, actual-phrase SRT, stale-audio rejection, and supplied-export timing comparisons. Added motion direction for rap density, story progression, refrain development, shaping-safe typography, offline audio reactivity, and the short proof before full production.

Publishing target: `rahulshahDEV/devotional-song-studio`. The user's conditional 10/10 requirement is preserved; completion of local tests does not certify live creative output. See `QUALITY.md` for evidence and blockers. GitHub network access failed during repository inspection; no commit/push has occurred.

## Setup and constraints

- Brave is installed at `/Applications/Brave Browser.app/Contents/MacOS/Brave Browser`.
- Python Playwright was not installed during planning. Install in a workspace virtual environment when browser work is requested.
- An ordinary Brave window cannot be attached unless debugging was enabled at launch. Reuse an authorized loopback endpoint or launch a dedicated workspace profile and have the user sign in there.
- Google's public documentation names the music generator **Lyria**, including Lyria 3 Pro. The requested name **Argon** remains unverified. Inspect the signed-in UI and resolve a material mismatch before substituting a model.
- Duration, languages, controls, and quotas must be checked in the account at production time. Do not promise seamless continuity across independently generated clips.

## First production run

Supply reference songs and the deity/subject. Bundle any other essential questions and infer ordinary creative details. No login, paid generation, video render, or publishing is part of creating this package.

## Verification

Validate the skill frontmatter and local links, compile the read-only browser probe, and exercise its argument handling and endpoint detection. A live run remains to be tested with a signed-in browser and actual reference songs.

Validation completed: skill validator passed; Python syntax, loopback restrictions, valid/malformed CDP fixture responses, output privacy, and local reference links passed. The live loopback probe was blocked by the session sandbox (Operation not permitted), so browser availability and Gemini execution remain unverified.

Improvement validation completed: skill validator and local reference links passed again. The video-folder helper passed isolated checks for directory layout, initial manifest state, preserving existing state/assets on resume, separate video folders, invalid slugs, and rejecting a symlink escape. No sample production folders were left in the workspace.

Behavioral review: the quality-review reference now defines ten regression scenarios covering narrow scope, inaccessible references, model mismatch, submission uncertainty, changed audio, separate videos, language-review limits, preparation-only release, visual-only edits, and browser attachment prerequisites. These are review cases, not evidence of live integration success. The next quality milestone is one complete production with real references, actual listening, verified rendering, and user feedback.
