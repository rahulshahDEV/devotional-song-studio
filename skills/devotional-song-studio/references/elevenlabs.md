# ElevenLabs route and capability checks

Research checked 2026-10-17 against the linked official documentation. Recheck the chosen product/model at execution: account access and interfaces can differ. The user permits ElevenLabs Music or Gemini for rap/song generation. This is the ElevenLabs route; a skill/documentation task alone does not authorize running generations, uploading audio, spending credits, or cloning a voice. Follow the actual production request and available authorized account/setup.

## Choose the product for the job

| Job | Candidate | Decision |
| --- | --- | --- |
| Finished rap/song with accompaniment | Eleven Music | Audition language, names, delivery, and coherence on actual output |
| Spoken prayer, intro, or narration | Text to Speech | Use compatible delivery controls; check the chosen voice in context |
| Preserve an existing performed delivery while changing voice | Voice changer | Test a clean performance excerpt; song suitability remains empirical |
| Recover material for a specific repair | Music stem separation | Check separation artifacts before committing |
| Draft timing for corrected actual words | Forced alignment | Review against the final audio; alignment is not transcription |

The [Music product guide](https://elevenlabs.io/docs/eleven-creative/products/music) describes vocal songs, section/lyric editing, and complex rap delivery. Its current model list includes Music v2 and v2.5. These are documented capabilities, not proof of convincing Hindi/Sanskrit performance or account availability.

## Music workflow

Use this route when ElevenLabs is chosen for the production, either by the user or within their allowed provider discretion. Preserve an already-selected provider unless the request changes it or an informed production decision resolves a blocker. Reuse the current song's lyrics, performance map, pronunciation ledger, and review criteria; do not start an unrelated production.

The [music prompting guide](https://elevenlabs.io/docs/overview/capabilities/music/best-practices) recommends deliberate genre, mood, instruments, tempo, production character, and ordered arrangement instructions. Its composition-plan option offers more structure than a prose prompt. In this studio, audition a concise brief first; add specificity to fix a demonstrated problem rather than accumulating adjectives.

Before submission save product/model, UI or API route, settings actually exposed, duration request, exact lyrics/prompt or plan, take lineage, and remaining authorized budget. Count section regenerations, variants, auditions, and service retries against that budget. Do not send multiple variants when only one submission's cost was authorized.

The [official API quickstart](https://elevenlabs.io/docs/eleven-api/guides/cookbooks/music) documents `music.compose`, `music.composition_plan.create`, and `music.compose_detailed`; `prompt` and `composition_plan` are alternative inputs. Use the live schema and installed SDK version. Do not mix fields from older section-based examples with a newer chunk-based schema. Save the returned plan/metadata separately from your intended arrangement; neither proves the words or timestamps actually performed.

Prefer an existing authorized UI session if that is the user's selected route. API use requires appropriate access and a securely configured key. Never store keys in prompts, manifests, screenshots, or release packages. No API call or live integration was tested as part of this documentation revision.

Inspect the real download codec, sample rate, channels, bitrate, and duration; do not promise WAV, stems, or a quality tier solely from marketing language. Retain the exact downloaded file and service/request identifier when available. Inspect an uncertain request before resubmitting.

## Speech delivery and pronunciation

The [TTS best-practices guide](https://elevenlabs.io/docs/overview/capabilities/text-to-speech/best-practices) distinguishes pronunciation approaches and model-dependent controls. Audio tags are supported by selected expressive models; SSML and phoneme compatibility varies. Recheck the selected model rather than transferring a tag or dictionary recipe between products.

For this studio, use speech synthesis for speech passages unless a real audition establishes that its musical delivery works. A spoken voice laid over a beat does not automatically become convincing rap. TTS controls should not be pasted into Music lyrics as if their interpretation were guaranteed.

Audition the same short, difficult passage in context before picking a voice. Begin with its default settings, then change one relevant control. Check diction, breath placement, emotional fit, identity consistency, and unwanted spoken stage directions. Keep useful surrounding context so line-by-line generation does not flatten the delivery. Tag only actual emotional turns; preserve an untagged reference. Do not assert a universal stability/similarity setting.

## Performance-led conversion

The [voice-changer documentation](https://elevenlabs.io/docs/overview/capabilities/voice-changer) describes preserving delivery and emotion from source audio and lists Hindi among supported languages. That is not a guarantee of pitch, diction, timing, or timbre on singing.

If the user has selected this approach, a well-performed original guide can supply phrasing that text-only direction misses. Use an authorized voice and source recording. Compare dry input/output for consonants, notes, timing, artifacts, and identity before mixing. Keep the original; don't convert a full backing track as if it were an isolated vocal.

## Stems and alignment

The [stem-separation API](https://elevenlabs.io/docs/api-reference/music/separate-stems) accepts audio for separation. Save outputs with the parent master identity and treat them as derived estimates. Follow the quality checks in [audio-production.md](audio-production.md); a separated stem is not automatically an improved master.

The [forced-alignment API](https://elevenlabs.io/docs/api-reference/forced-alignment/create/) aligns supplied audio with supplied text. Correct the actual-sung transcript first. Mark repeated phrases, sustained syllables, code-switches, uncertain words, and ad-libs for review. Do not force absent intended lyrics onto the waveform. Listen around word boundaries; keep uncertainty explicit when translating service output into [rap-sync.md](rap-sync.md). Do not set reviewed flags merely because a service returned timestamps.

Provider jobs and local alignment tools are alternatives chosen for the task, not mandatory paid steps. No service is required just to revise lyrics or motion guidance.
