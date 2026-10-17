# A motion.md that directs an actual music video

Read with [motion-direction.md](motion-direction.md) when planning a video. Save the production-specific `motion.md` inside its dedicated video folder. It turns the selected song, storyboard, and reviewed timing into an executable visual plan. Do not create video folders for a skill-only review.

## Write these decisions before building scenes

- **Meaning:** the song's emotional change and a visible motif that changes with it.
- **Visual grammar:** palette, local fonts and script coverage, image treatment, depth, negative space, and what earns a camera move.
- **Section contrast:** how verse, refrain, prayer, and climax differ; choose a few complementary rules from the installed animation skill.
- **Typography:** actual sung phrases, measured line breaks, hierarchy, contrast and phone readability; preserve Indic shaping.
- **Cue ownership:** reviewed vocal/narrative/beat anchor IDs from `sync.json`, source offset, absolute landing time, and scene-local conversion.
- **Implementation:** installed registry items, asset paths/provenance, scene IDs, timeline ownership, and runtime/version.
- **Proof and review:** difficult excerpt, export observations, failures, corrections, and remaining unreviewed items.

Keep exact timestamps in the reviewed sync data; refer to cue IDs here instead of maintaining two editable timing authorities.

## A useful choreography table

| Section / cue | What changes and why | Focal action | Motion envelope | Readable hold / exit |
| --- | --- | --- | --- | --- |
| Confession / reviewed vocal phrase | A constrained path expresses the narrator's hesitation | One image and a stable lyric phrase | Slow restrained push; no beat bounce on text | Hold through the phrase, leave after comprehension |
| Resolve / reviewed narrative anchor | The path gains direction as the narrator chooses action | A meaningful reveal | Anticipation begins before the anchor; reveal lands on it; settle | Leave room for the next lyric |
| Refrain / reviewed musical anchor | Return to the same motif with a changed state | A clear recurring image | Wider space and stronger but bounded movement | Stable central phrase; transition with handles |
| Fast passage / reviewed vocal groups | Attention stays on meaning at high density | One readable shaped phrase group | Quiet camera, selective emphasis | Replace by reviewed phrase groups; never every syllable |
| Ending / reviewed tail | Resolve the image with the completed prayer | A resting composition | Movement decays with musical energy | Preserve the actual audio tail |

Replace these examples with the chosen story. Avoid literal illustrated substitution for every word and avoid repeating identical shots on every refrain.

Choose purposeful transition logic: continue a shape, move through shared depth, or reveal a narrative consequence. Search the installed registry before implementing named treatments. Reserve larger movement for structural change. Dhol/snare accents can receive brief decor; lead syllables govern lyric emphasis. A decorative onset is not a lyric timestamp.

## HyperFrames implementation checks

Load the current HyperFrames entry, core, animation, and CLI skills; load keyframes, registry, studio, or audio for the relevant operation. Local guidance describes the installed contract, not a permanently pinned API.

- Use framework-owned timed clips and media. Each audio element needs a unique ID. Do not drive playback with `audio.currentTime`, `play()`, or a second clock.
- Register one completed paused timeline per composition under its matching composition ID. Let the framework nest sub-compositions; do not also nest their timelines manually.
- Animate inner visual wrappers. Keep framework clip visibility separate from GSAP motion; avoid competing CSS and GSAP transforms on the same property.
- Make scene offsets explicit: local event time = absolute audio time minus scene start. Preserve excerpt source offsets. Use absolute cue quantization from the sync compiler instead of adding rounded bar durations.
- Load local assets/fonts before layout measurement. Check whole Hindi phrases at target size; splitting matras, conjuncts, or arbitrary letters can break shaping.
- Precompute audio features and evaluate them at timeline time. Avoid live analysers, wall clocks, unseeded randomness, or callback-only motion that fails on seeking.
- Record the CLI/runtime version used. Follow the entry skill's current project upgrade policy; validate and compare important frames after a version change.

These choices follow the installed core contract and the [official HyperFrames core documentation](https://github.com/heygen-com/hyperframes/blob/main/packages/core/docs/core.md). The [rendering explanation](https://www.heygen.com/research/html-to-video) explains why independently seekable frames matter.

## Prove the difficult part

Render a 10–20 second passage covering a fast lyric and an earned landing. Inspect target frame and adjacent frames; seek to the same point from earlier and later positions. Compare appearance, text shaping, and cue landing. Watch with audio at delivery size and on a phone-sized preview.

Run the current CLI lint/check flow and confirm actual runtime/layout/text samples ran. A lint error can prevent later audits; zero samples is not a clean visual review. Fix errors, inspect snapshots, then review a real encoded proof. Build the rest only after the proof resolves the difficult issue.

For the final export, record observed anchors throughout start/middle/end and the fastest section. Inspect offsets, cumulative drift, lyric dwell time, transition continuity, source audio identity, and tail. Keep machine pass, visual pass, and listened synchronization review separate in the evidence.

Follow the loaded workflow's actual render approval requirements and any existing user authorization. A skill/documentation improvement does not itself authorize rendering or publishing a new video.

## Continue in another AI code editor

Follow [editor-handoff.md](editor-handoff.md) when the target editor cannot discover the entry or owning workflow. It distinguishes standalone installation recovery from plugin-managed bundles.

The user permits ElevenLabs Music or Gemini web for song generation, Gemini or ChatGPT web for images, and requires HyperFrames motion graphics for visuals. Open the repository in the chosen editor and have its agent read the main SKILL.md, studio-preferences.md, this plan, and the current production/video manifests. Follow the same instructions even when the editor has no dollar-prefixed skill invocation.

Keep the handoff self-contained: relative local assets/fonts, selected audio identity, lyrics/transcript, reviewed sync.json, motion.md, storyboard, editable HTML/CSS/JavaScript, dependency manifest/lockfile when present, and actual validation/resume status. Record any required runtime setup without copying credentials or browser profiles. A capable editor needs file and terminal tools plus the project's dependencies; do not claim all editors have been tested.

Use the installed motion-graphics workflow for short units within its supported scope. Full-song assembly remains under the appropriate HyperFrames owner while using the same motion-graphics design language and audio clock. Keep all of it in the video's dedicated folder.

## Image generation for this studio

The user allows image generation at https://chatgpt.com and https://gemini.google.com. Use an available authorized browser workflow for the chosen site; inspect actual controls rather than assuming an API or model. Record the chosen site, prompt, reference images, observed result, and downloaded local asset. If access is unavailable, preserve the prompt and report the blocker. Music generation is independently allowed through ElevenLabs Music or Gemini.

Before generating, define a compact visual reference: subject/character appearance, clothing and identifying details, devotional depiction choices, palette, lighting, medium, camera framing, and compositions that leave room for lyrics. Reuse the approved reference image when the site's controls support it. Evaluate consistency across shots, anatomy and symbolic details, crop, and text clearance. Keep captions as editable shaped text in HyperFrames rather than relying on generated lettering. A beautiful isolated image is insufficient if it breaks continuity or cannot support the planned motion.
