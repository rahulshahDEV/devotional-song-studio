# Craft review and completion checks

Use the relevant review before proceeding to work that depends on it. Reviews are working decisions; user approval is needed only where their request or an actual external-action boundary requires it. Judge evidence rather than claiming a numerical score proves quality.

## Lyrics before audio submission

- **Story:** the opening establishes a person/place/question; verses cause change; the ending answers or transforms the beginning. If an anthem or meditation intentionally has no plot, assess its emotional progression instead.
- **Devotion:** the subject shapes the language, imagery, and choices. Scripture/source claims are distinguished from poetic invention. The narrator's voice stays coherent.
- **Hook:** a listener can understand and remember the central phrase; repetitions gain energy or meaning. Compare candidates and state why the chosen one fits.
- **Performance:** natural idiom, speakable lines, breathing room, intentional rhyme and clear sacred names. An unfamiliar language gets explicit confidence limits.
- **Originality:** reference traits were transformed into original choices. No obvious copied distinctive lines/hooks or source-dependent gimmick.

Record the weakest part, a concrete revision, and any intentional tradeoff. Do not endlessly polish: use one focused revision pass, then another only for an unresolved defect or specific user request.

## Audio before timing lock

Listen to the beginning, every verse/refrain transition, pronunciation-sensitive passages, bridge/climax, and ending; review the full track when possible. Compare actual sung text with intended critical lines. Inspect decodability, duration, obvious truncation, unwanted long silence, and audible distortion with suitable tools. Signal checks do not prove emotional quality.

State a take's strongest feature, most material weakness, and why it is selected over alternatives. Missing story resolution, severe central-name errors, or a broken ending prevent calling it final. If all budgeted takes are unsuitable, preserve them, explain the specific defect, and ask for a budget/style decision instead of silently submitting more.

## Video before final render

Use [rap-sync.md](rap-sync.md) to review musical, vocal, and narrative anchors separately and [motion-direction.md](motion-direction.md) to define the visual system. Check a short difficult passage before building the full composition. Preserve the actual reference/source versus estimated/reviewed status of timing data.

Check the storyboard against actual song sections. Inspect representative frames from intro, verse, refrain, climax, and ending, plus transitions and the densest text. Check Devanagari/other script shaping at final size, useful contrast, relevant imagery, visual consistency, and actual crop. Repeated refrains should develop a visual motif rather than fill time with unrelated stock assets.

Review a preview with audio for narrative coherence and synchronization. Verify a rendered file's actual audio/video streams, duration, ending, caption timing and aspect ratio. An unavailable viewer/listener must result in an explicit unreviewed item. A render-success exit code does not establish visual quality.

Inspect actual exported events at the start, middle, end, fastest verse, and repeated refrain. Record observed event timestamps and compare against intended cues using the sync compiler. Inspect constant offsets, accumulating drift, and isolated word errors separately. No observations means unverified; partial coverage must remain partial. Frame tolerances are studio targets, not claims of proven perceptual accuracy.

## Release readiness

Confirm the file matches the reviewed export, captions match what is sung, the thumbnail/title represent the video, and source credits are accurate. Keep unknown rights/settings explicit. Verify user-authorized channel/visibility and current disclosure requirements during release work.

## Regression scenarios for skill revisions

Use these cases as a behavioral review; do not treat a prose walkthrough as a live integration test.

| Request or event | Expected behavior |
| --- | --- |
| “Only write a Hindi Hanuman rap; no video yet.” | Write/review lyrics; no Gemini submission or video scaffolding |
| “Use these three rap references,” but links cannot be opened | State access limitation; analyze available transcripts/descriptions without claiming listening |
| “Use Argon,” but Gemini shows only other music choices | Save requested/observed labels; continue lyrics; resolve choice before substitution |
| Submission times out after Send | Mark pending/unknown and inspect existing result; do not immediately resend |
| Song audio is replaced after captions exist | Preserve prior work and mark dependent timing/captions/renders stale |
| “Make two different videos for this song.” | Create two video folders before video work, each with local assets/project/exports |
| “Create a Tamil song,” with limited pronunciation tools | Preserve Tamil, adapt idiom, disclose review limits; do not claim native fluency review |
| “Prepare for YouTube; don't upload.” | Finish the local release package; perform no upload/publication |
| “Just change the video colors.” | Resume that video's folder; edit visuals and validate; no audio regeneration |
| “Use my open Brave session,” without debug port | Explain attach prerequisite; preserve existing browser and offer dedicated profile setup |

For an end-to-end claim, separately require observed live browser attachment, actual generation/download, listened-to audio, rendered/reviewed video, and requested upload verification. Local fixtures cover helper behavior only.

## Evidence-based quality rating

For a skill audit, rate written workflow separately from delivered art. A complete instruction set cannot establish realistic vocals. Save the review date, inspected files, available artifacts, score rationale, and top defects. Do not increase a score just because guidance was added.

For an actual song, score each observed dimension from 0–10 and record a timecode/example plus the next improvement. Use these studio weights as a diagnostic, not a scientific measure:

| Dimension | Weight | What earns a high score |
| --- | --- | --- |
| Devotional meaning and specificity | 15% | Subject shapes the choices; central source claims and names are sound |
| Story and original lyrics | 15% | Concrete images, causal/emotional change, earned ending |
| Hook and musical development | 15% | Memorable refrain; meaningful contrast and return |
| Flow and performance realism | 20% | Believable intention, breath, cadence, diction, consistent voice |
| Pronunciation and actual lyric fidelity | 15% | Critical words clear; no missing story resolution |
| Production and finish | 20% | Intelligible lead, coherent arrangement, clean transitions and tail |

For a requested video, score separately: meaning/art direction 25%, choreography/section contrast 25%, typography/readability 20%, observed synchronization 20%, and export integrity 10%. Do not let video polish hide a weak song.

Compute a weighted total only when all its dimensions were reviewed. Otherwise mark the total unverified; a rubric walkthrough or signal analysis cannot fill missing listening/viewing scores. Record who listened and under what conditions. A native-speaker review, phone check, or blinded comparison counts only when it occurred.

Aim for 10/10 through concrete revisions, but never label unobserved quality perfect. A critical pronunciation error, clipped ending, obvious synthesis defect, missing lyric resolution, or unreadable/broken caption blocks final readiness even if the weighted average is high. Stop service retries at the authorized budget, retain the strongest honest candidate, and record the remaining decision.

For listener feedback, use specific questions: which phrase felt artificial, where meaning became unclear, whether the hook stayed memorable, and whether the ending felt earned. Use their timecoded feedback to select the next repair. Do not ask only whether they “liked it.”

## Additional behavioral review cases

| Request or event | Expected behavior |
| --- | --- |
| “Research ElevenLabs and improve the skill.” | Update guidance and sources; no paid generation or silent provider migration |
| “Use ElevenLabs for this song instead of Gemini.” | Select the permitted ElevenLabs route for this production; check live capability, preserve budget and provenance |
| A TTS tag or phoneme recipe is proposed for Music | Check product/model support; do not assume shared syntax |
| A plan returns exact-looking section timestamps | Keep them planned until verified against audio |
| New master after vocal repair or normalization | Preserve old master; recheck identity and invalidate dependent timing |
| A separated vocal sounds watery | Keep original; reject separation for the mix if it degrades the result |
| HyperFrames check reports zero samples | Inspect preceding errors; do not call the visual audit passed |

## Forward-test findings and corrected behavior

A read-only independent exercise used a Hindi Hanuman worker-to-service brief, a verse-only revision, and an editor handoff with missing HyperFrames skills. It produced an original draft and image/motion plan; it did not generate or score actual audio/video.

| Request or condition | Behavior to preserve |
| --- | --- |
| Generic “use Gemini” with no named model | Inspect and use the available music tool; do not block on historical Argon wording |
| “Revise only verse two; leave audio/video intact” | Save an unsung lyric draft; retain performed transcript, selected master, captions, cues, and renders |
| HyperFrames skills missing in another editor | Use editor-handoff.md to recover the correct standalone/plugin instructions; continue independent work, keep render unverified |
| Image generation at ChatGPT/Gemini | Save local downloads and consistent visual references; record the independently selected ElevenLabs/Gemini music route |
