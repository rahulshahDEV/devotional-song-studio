# Video and release handoff

## Visual production

Before any video work create its dedicated folder as defined in [production-contract.md](production-contract.md). All paths below are relative to that folder. Begin from selected, reviewed audio copied to `audio/` with its source fingerprint recorded. Keep its duration and timing as the source of truth. Save:

- `transcript.md`: actual sung words, including ad-libs; mark uncertain words for review.
- `captions.srt`: checked timings from the actual performance. Do not manufacture word-level synchronization if only section timings are available.
- `beat-map.json`: measured or estimated beats, section boundaries, and confidence.
- `storyboard.md`: scene start/end, lyric/story beat, image or symbol, composition, transition, and asset source.
- `motion.md`: the concrete visual grammar, section choreography, cue references, runtime choices, and proof/review findings from [motion.md](motion.md).
- `project/`: HyperFrames project and its current brief/state. Keep previews in `previews/` and deliverable renders in `exports/`.

Author the requested motion graphics as an editable HyperFrames code project in the user's chosen AI code editor. Use the available HyperFrames entry skill first. Resolve the owning route it specifies. A full beat-driven song normally uses music-to-video; short teasers can use motion-graphics, and custom narrative pieces may use general-video. Read core before authoring HTML and registry before implementing named effects. Use media-use for assets and captions as appropriate. Follow the owning workflow's actual dependencies; do not run HyperFrames commands from memory if its skills are missing.

Choose a coherent treatment appropriate to the tradition: illustrated story scenes, symbolic landscapes, expressive typography, or a combination. Respect the user's preferences about depicting deities. Avoid treating sacred symbols as arbitrary decoration. Invented visuals should not be described as historical evidence.

Match motion to musical function: establish place in the intro, advance the story in verses, return to a recognizable visual motif in refrains, and resolve it at the ending. Cut on meaningful accents rather than every detected beat. Use readable text blocks and preserve Indic shaping, vowel marks, and conjuncts; animate whole words or lines if letter splitting breaks the script. Do not invent word timing to support kinetic text.

Default YouTube master target: 1920×1080, 16:9, H.264 video with AAC audio in MP4. Use the composition's chosen frame rate consistently. A requested Shorts derivative targets 1080×1920 with a deliberate reframe and a coherent hook excerpt. These are production defaults; check current upload requirements before release.

Verify renders through the current HyperFrames checks and representative snapshots. Inspect text legibility/shaping, image rights/provenance, start/end, scene transitions, crop/safe zones, caption sync, audio continuity, clipping, and final file duration/streams. Keep the chosen full-song audio intact unless an edit is requested. Document anything that cannot be viewed or heard.

## Release package

Create `release/` with title options, a recommended title, description, credits/provenance, thumbnail brief/image if requested, captions, and `upload-settings.json`. Record the intended video path, channel, language, visibility, audience setting, synthetic-media disclosure, and schedule including timezone. Unknown choices stay unknown.

Titles should accurately describe the song's deity/theme and language. Descriptions distinguish original poetic storytelling from scriptural quotation and include verified source credits. Do not promise monetization, royalty-free status, or exclusive ownership without evidence. Check the selected music/image providers' applicable output terms and source-asset permissions before making commercial-rights claims.

YouTube's disclosure guidance lists synthetically generated music as an example requiring disclosure. Verify the current guidance and represent this honestly in upload settings. Do not assume an AI disclosure in the description substitutes for the platform's disclosure field. Devotional subject matter alone does not determine whether content is made for kids; use its actual intended audience.

## Upload or publishing actions

Follow the exact user-requested action. An upload request is not automatically a public-publish request. Use authorized visibility or obtain the missing choice after the package is reviewable. If the user has already authorized the exact upload/publish scope, proceed without another confirmation.

If uploading through Brave/Playwright, inspect current YouTube Studio controls and the channel identity, use the actual file picker, and verify progress/completion. Do not assume the Gemini tab's account implies the correct YouTube channel. If an official connected upload tool is available and the user has no conflicting browser preference, use it within existing authorization.

Save the resulting video ID/URL, visibility, schedule timezone, and observed processing/checks state. On uncertain submission, inspect existing channel uploads before retrying to avoid duplicates. Do not delete/re-upload, dispute claims, or change channel-wide settings as an implicit repair. Report unresolved processing or copyright checks accurately.

## Sources to refresh at release

- [YouTube: Disclosing altered or synthetic content](https://support.google.com/youtube/answer/14328491?hl=en).
- [YouTube: Recommended upload encoding settings](https://support.google.com/youtube/answer/1722171?hl=en).
- [Google: Gemini Apps terms and related policies](https://gemini.google.com/terms).
