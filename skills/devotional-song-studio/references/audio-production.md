# Performance, realism, and audio finishing

Read before prompting or selecting a song. These are studio decisions to audition, not guarantees about a generator.

## Make the delivery believable

Build a performance map alongside the lyrics: section, intention, vocal register, rhythmic feel, breath points, lead/double/response role, and arrangement change. Direct an action (“confessing quietly, then resolving to act”) rather than stacking “epic, soulful, realistic, cinematic.”

For rap, speak the verse over the intended pulse. Mark stressed words, pickups, pauses, and places where consonants collide. Preserve natural Hindi stress and meaningful sacred names before increasing rhyme density. Alternate longer runs with short answers; a fast passage should express urgency in the story. Avoid equal syllable counts and identical cadence on every line.

For a melodic refrain, simplify the text enough to sustain vowels without obscuring meaning. Let the lead state the prayer before adding responses. Support a convincing lead with selective doubles or harmonies; do not bury weak pronunciation in a crowd.

Use intentional human detail: a plausible breath at a phrase boundary, a restrained change in intensity, a slightly delayed response. Preserve convincing variation already present. Random timing jitter, fake inhalations every bar, distortion, and permanent vibrato do not establish realism. Avoid changing the singer's apparent identity between sections.

Keep a pronunciation ledger in `pronunciation.md`: written word, intended pronunciation and meaning, language/tradition, review source, attempted spelling/direction, heard result, and unresolved issue. Test difficult names inside a real phrase. Keep display lyrics canonical; generator-only respelling belongs in the submission copy. Native-language text is the starting point, not an assurance of correct pronunciation.

## Arrangement with room for the story

Choose a few complementary instruments and define their jobs: pulse, bass, devotional identity, melodic response, atmosphere. A traditional instrument needs a musical role rather than a list of culturally associated sounds. State when layers enter and leave. Remove busy parts under dense rap; let the refrain expand through contrast.

Write planned bars and duration as estimates. For a constant 4/4 pulse, seconds per bar = 240/BPM; 8 bars at 90 BPM is about 21.33 seconds. Pickups, rubato, and holds change this. Measure the result before using it as a timing source.

Keep one production identity across sections: lead voice, tonal center when relevant, room, and core groove. For section repairs compare the surrounding bars as well as the changed lyric; listen for altered voice, key, ambience, groove, or level. An intended tempo is not a measured beat map.

## Audition and repair within budget

When supported and authorized, a short test containing the hardest name, fast cadence, and hook can reveal a bad voice/direction before a full song. It consumes the existing submission budget. If the tool produces only full takes, evaluate those rather than inventing unsupported controls.

For each retry record the defect and one main change. Compare equivalent excerpts at matched perceived loudness, with filenames hidden when practical. A louder take should not win automatically. Listen to the complete candidate after an excerpt wins: isolated excellence can conceal a repeated verse, identity change, or broken ending.

Prefer a local section revision when the provider supports it and the rest works. Preserve the parent take and exact edit region. Otherwise choose a new full take or accept a documented limitation. Do not splice incompatible performances merely to claim every lyric is present.

## Mix according to available material

With only a stereo master, begin with conservative level management and comparison. Broad EQ/compression affects voice and instruments together. It cannot repair a mispronounced name, rewrite lyrics, or recover missing frequencies. Preserve source bytes and work on derivatives.

With useful stems, first check bleed, watery consonants, cymbal damage, phase, channel count, lengths, and common start offsets. Recombine at the supplied gains and compare with the source. Separation estimates are not clean multitrack originals. Keep stems only when they improve the result; using a vocal stem for alignment does not make it suitable for the final mix.

For a stem mix, set balance before processing. Keep the lead intelligible, preserve breaths that serve phrasing, control intrusive sibilance locally, and use only enough compression to keep meaning audible. Make space in instruments rather than repeatedly boosting vocal brightness. Add short room/reverb or phrase-end delay when the scene needs it; keep fast consonants clear. Ad-libs answer the lead without covering the next line. Check bass and intelligibility in mono.

Use EQ, de-essing, compression, saturation, pitch correction, or limiting only for an audible problem or chosen aesthetic. Save the reason and a level-matched bypass comparison. There is no universal frequency cut, compressor preset, or “realism” chain.

## Finishing and listening evidence

Measure the decoded source with the existing `analyze_audio.py` helper; consult its CLI help and record unavailable optional dependencies. Use integrated loudness, loudness range, and true peak as diagnostics. If normalization is needed, FFmpeg supports measured two-pass loudnorm; inspect whether its linear mode was feasible. Choose a delivery target for this project rather than declaring a universal streaming LUFS rule. See [FFmpeg filters](https://ffmpeg.org/ffmpeg-filters.html#loudnorm).

Keep a lossless working derivative when processing, while preserving the highest-quality actual download. MP3 converted to WAV remains a lossy source. Minimize repeated lossy encoding. Inspect the encoded delivery too: codec conversion can change peaks and reveal artifacts.

Listen on headphones, a phone or small speaker, and in mono when those checks are available. At quiet playback, can the story and names still be understood? At transitions, are there clicks, pumping, ambience jumps, or missing tails? Note exactly which devices/checks were actually used.

Save `mix-review.md`: source identity, processing and purpose, before/after measurements, checked timecodes, listening conditions, selected version, unresolved defects. Only a listened-to finished master can establish the audio lock. Copy that exact version into the video and invalidate earlier timing if it changed.

## Example performance brief

Adapt this original direction to the subject and provider; it is not a fixed musical formula:

> Hindi devotional storytelling rap; intimate contemporary hip-hop, around 90 BPM in a half-time feel. A close, conversational lead begins with uncertainty, becomes firmer through the second verse, and opens into a simple melodic prayer. Sparse hand percussion and bass support the verse; a restrained harmonium response answers the hook. Keep the central name unhurried and intelligible. Leave air after the turning-point line. Final refrain feels earned; preserve a complete vocal and instrumental tail.

Put exact lyrics separately from directions. Replace every generic intention with story-specific details before submitting.
