# Art direction and motion for devotional rap

Use [motion.md](motion.md) for the production-specific plan, choreography table, HyperFrames implementation checks, and proof evidence. This document owns the artistic principles; the plan translates them into the actual song.

## Design a visual idea before effects

Write one sentence connecting the song's change to a visible change. For example: “A tangled path becomes navigable as the devotee changes their actions.” Build a motif from that story instead of cycling unrelated deity images. Record depiction preferences before producing imagery when they materially affect the concept.

Create a small visual system in the video's design notes: one display/text font pairing with verified script coverage, a restrained palette, text hierarchy, repeated motif, depth/camera language, transition logic, and the role of silence/negative space. Render a dense Hindi line and a sensitive name at final resolution before committing the font. Ship local fonts with provenance; wait for font readiness before measuring layout.

Choose 2–4 complementary motion rules per scene through the installed HyperFrames animation skill. Search the registry before building named treatments. Avoid adding effects because the soundtrack is fast; make each major motion advance meaning, focus, or musical punctuation.

## Choreography by song function

| Song function | Visual job | Timing approach |
| --- | --- | --- |
| Opening/pickup | Establish the question and a concrete image | Let the pickup precede the first strong landing; do not force a title to beat zero |
| Story verse | Make an action or consequence understandable | Phrase-driven scenes, selected rhyme accents, readable lyric holds |
| Double-time passage | Preserve comprehension at high vocal density | Stable camera/text block with selective word emphasis; fewer competing layers |
| Pre-hook | Build expectation | Compress space or simplify palette; save the strongest visual reveal |
| Hook | Deliver a repeatable emotional image | Return to a motif with a changed state; land major reveals on reviewed anchors |
| Prayer/breakdown | Give the voice and meaning space | Hold, slow camera movement, reduce amplitude and text motion |
| Final refrain | Resolve the motif and story | Develop the earlier image rather than replaying the same shots unchanged |
| Outro | Finish with an intentional visual resting state | Respect the audio tail; no abrupt freeze/cut or unsolicited long end screen |

These are creative options, not a mandatory structure. A meditative song may need restrained motion throughout.

## Hierarchy and kinetics

Keep one dominant focal action at a time. Use secondary motion at lower amplitude; reserve the strongest scale/contrast/camera moves for earned moments. For an impact, anticipation → landing → settle has a clear anchor. Begin anticipation early enough that the landing matches the sound. Use contrasting motion density between sections so the refrain has somewhere to grow.

For Hindi, animate whole words/phrases by default. Do not wrap code points or arbitrary grapheme clusters into separate spans and assume Devanagari shaping survives. Keep conjuncts, matras, and headline connections intact. If a word changes color, retain a single shaped text run or verify a shaping-preserving overlay at actual size. Avoid random font fallback and aggressive letter spacing.

Test lyric readability at both the intended full frame and a phone-sized preview. Dense rap may need grouped phrases, less text, or a quieter background. Never shrink text repeatedly to preserve an overcrowded layout. Position meaningful line breaks from actual rendered measurements rather than a universal character count across languages.

For beat-reactive decor, derive a bounded smoothed envelope from precomputed features; it should support the song, not compete with the singer. Do not drive every object from the same RMS value or create a fake random equalizer. Use offline features and timeline time; live Web Audio/clock/random state cannot guarantee identical rendered frames. No strobe is needed to express intensity.

## Build a short proof before full production

Choose a 10–20 second span containing a difficult fast line and an important musical landing. Create it inside the video's existing folder. Check typography, scene layering, cue timing, and deterministic seeking. If this span fails, correct the visual system/timing before expanding to the full song. This is a production tactic, not an extra approval gate.

Represent the song's full emotional range in the storyboard; the hardest span alone does not prove the full narrative works. For Shorts, choose a coherent passage and recompose for portrait; preserve its actual source offset in all timing data rather than blindly cropping the master.

## Final review

Preview with audio, then inspect exported output. Sample an event at its preceding frame, target frame, and following frame to verify the landing. Seek to the same timestamp from different positions; matching appearance is evidence of deterministic choreography, not evidence of lyric accuracy. Check that every transition has adequate handles and scene timing remains local/absolute as intended.

Keep a concise review record: craft weakness, timecode, observed evidence, concrete fix, and recheck result. A visual should survive removal of decorative effects: the story, hierarchy, and typography should still communicate.
