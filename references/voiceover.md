# Natural female voiceover

Female narration is part of this skill's default video deliverable, not an optional silent omission.

## What “human female voice” means in practice

1. **Supplied human female recording:** use and edit that real recording. Keep its source identified as `human-recording`.
2. **Natural female AI voice:** when the user means human-like delivery and an appropriate TTS tool is available, synthesize with an adult female voice supporting the target language. Identify the source as `ai-tts`; do not call a synthetic voice an actual human recording.
3. **Actual human required but no recording available:** request the recording or explain that a voice artist must supply it. Prepare the script and visual work meanwhile. A skill cannot provide an unrecorded human performance by itself.

Use a supplied human recording first. Otherwise the practical fallback is natural female TTS, disclosed as synthetic. If the user explicitly insists on a real human, do not substitute TTS. Voice source can be clarified with the product brief rather than repeatedly asked for on every revision.

## Tool and capability checks

- Inspect available audio/TTS tools and configured services before choosing a provider. This skill requires no particular provider and bundles no credentials or voice subscription.
- Select a voice that actually supports Hindi/Hinglish, English, or the requested language. Listen to a short sample for female presentation, pronunciation, warmth, and intelligibility.
- Use an available service within the user's authorized access. Never invent a voice identifier, completed audio file, or successful API call. Do not expose API keys in project output.
- When no suitable voice tool or recording is available, save the narration script, mark voiceover `pending`, and clearly label any visual preview as silent. An audio stream or a tone is not proof of female narration.

## Script and delivery

Follow the audience's language and the selected style's delivery notes. Hinglish is appropriate when established by the conversation; use natural spoken phrasing rather than a literal translation of an English ad.

Write a short hook, product name, supported benefits, and CTA. A 30-second promo often starts around **50–65 spoken words**, leaving room for pauses; use actual recorded duration, not a word-count guess, to set the final timing. Fast styles can use fewer pauses but should still sound human and clear.

- Use the intended script for the voice engine, often Devanagari for Hindi words and Latin letters for brand names. Check pronunciation rather than assuming mixed scripts always work.
- Captions may be Hindi, English, or Romanized Hinglish according to the brief. Their script does not have to match the TTS input script; their meaning and timing must match the audio.
- Add pronunciation notes for brands, units, or acronyms. Test troublesome terms in the short sample before generating the whole narration.
- Keep delivery conversational, with natural emphasis and pauses. Prefer shortening copy over speeding audio unnaturally. Do not clip the final syllable to meet the target duration.

## Timing, captions, and mix

Generate or obtain the real audio before locking the animation and captions. Measure its duration. Use provider timings or an available alignment/transcription tool when accurate; otherwise manually align phrase boundaries by listening. Label estimated timings as provisional until checked.

Preserve one voice identity and pronunciation across the sample and full video. The preview's voice sample should come from the same script/delivery approach as the final track.

Mix voice clearly above music and sound effects. Duck music during speech, use short fades, avoid clipping, and listen on phone speakers. Optional project mix targets are around -14 to -16 LUFS integrated with a true peak below -1 dBTP; these are production targets, not YouTube requirements, and require real measurement before reporting compliance.

Save a clean voiceover file and an SRT or VTT file when produced, alongside the video source. Record provider/voice identity, language, source type, and actual audio path in the working brief. A final video awaiting required narration remains incomplete; explain that status rather than presenting it as fully voiced.
