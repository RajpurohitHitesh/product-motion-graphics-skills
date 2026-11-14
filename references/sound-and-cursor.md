# Music, tactile effects and pointer choreography

Use when producing the selected style's preview/final audio and interaction cues. The three [archived reference players](source-prompts/PROVENANCE.md) contain working synthesized scores and cursor helpers. Their score code and diagnostic render buffers were inspected; the comparison did not include a listening review. Reuse a relevant implementation when available, then judge the actual new mix by listening.

## Music direction by treatment

| Treatment / style fit | Bed and rhythm | Phrase shape |
| --- | --- | --- |
| Creator, mainly 6/8 | Low, restrained electronic pulse or half-time rhythm; stronger accents reserved for key landings | Brief hook lift, stable body groove, space around the important number, clean resolving takeaway |
| Clean Tech, mainly 1/3/5/7 and light 6 | Warm/airy pad, sparse percussion; optional light kick for an energetic demo | Let the title breathe, sustain quiet momentum, resolve a real completion with a short chord/chime |
| Walkthrough, mainly 2/3 | Calm pad with light hats or no percussion; tactile actions remain easy to hear | Title opening, low bed through steps, small step transitions, clear outcome hold |
| Layered app / 4 | Light brand-compatible electronic bed with restrained card-swap accents | Build into the hero, reduce activity during feature reading, resolve on the product |
| Cinematic / 9 | Sparse sustained atmosphere and material/reveal accents | Gentle buildup, space for detail/narration, grounded hero finish |
| Dark launch / 10 | Restrained dark electronic texture, warm low pulse and selective bright accents | Support input → action → result, with a short lift into the genuine output |

These are composition directions, not fixed BPMs or a reason to reuse the sample's exact tune. Adapt the mood to the product and requested energy. Keep a coherent harmonic/rhythmic bed across scenes; vary density at idea boundaries rather than restarting unrelated tracks. Provide a clean onset and ending without abrupt truncation. Use user-supplied/licensed music or an available procedural implementation as appropriate.

## Score the actual interaction

Drive sound from the same [event map](motion-craft.md) as the picture: focus move, pointer approach, activation, typed interval, supported state change and result hold. A starting vocabulary:

- **Click/tap:** short rounded tactile transient at the visible activation; mobile may use a softer touch sound.
- **Typing:** quiet varying key taps confined to visible character entry, with a small natural pause before submission.
- **Panel/card/menu:** soft pop or short airy movement, proportional to the visual event.
- **Step change:** optional small two-note motif; keep it subtler than a completed-task chime.
- **Focus/camera:** low soft swell when the move needs an accent; a silent focus move is often sufficient during narration.
- **Actual saved/completed result:** brief resolving chime. Notification ping only when a genuine notification is shown.
- **Creator keyword/metric:** restrained swipe or occasional impact on the important landing. Keep counter ticks sparse and linked to displayed value changes.

Use a small related sound family. Not every text entrance needs a tick, and each ordinary click does not need a success chime. Inspect sounds through real device speakers as well as headphones where possible. Avoid sharp repetitive beeps, excessive low-frequency impacts and sustained effects over control names or numbers.

## Voice and mix

Keep music, action effects and narration independently controllable. When speech is present, lower the bed beneath it and recover smoothly through pauses; retain clear clicks without masking consonants. Verify headroom on the combined master, not just on each separate stem. Match perceived level across scenes and listen for clipping, pumping, abrupt cuts, ringing tails and loops.

When the user will add ElevenLabs audio later, use an empty narration track and an appropriate quiet bed/effects mix, preserving scene/event markers for realignment. No generated speech or vocal samples should appear in a no-voice brief. The reference's helper named `voice` is a synthesizer oscillator, not narration. A functioning audio buffer does not prove good loudness or a pleasant mix.

## Cursor and mobile touch

For a real desktop flow, use a clear arrow with eased waypoint travel. Approach the actual control, settle briefly, press/dip, then let the next state register before moving again. Cursor scale and contrast must remain useful at the final crop. Avoid wandering between actions or leaving the pointer covering the label the viewer needs to read.

For phone screenshots, use a small touch ripple or brief fingertip cue when appropriate; do not add desktop-window chrome simply to reuse the reference helper. A screen-space step pill can stay fixed while the source-space control and touch cue move together under the camera.

Store each activation's origin at the control's **event-time position**. An expanding click ripple stays at that point as the pointer leaves, and follows the source transform if its screenshot moves; do not recenter every active ripple on the pointer's current position. Keep approach, press, visual feedback and click sound on the same event.

Immediate visual feedback must be supported by source states or real footage. The sample's fast pressed/selected response does not authorize invented app performance, success banners or delivered notifications. A screenshot-composed walkthrough uses illustrated interaction cues; it is not a screen recording of live execution.

## Preview and seek checks

In a representative action/result preview, watch and listen to approach → activation → typing/state → outcome. Verify ripple location after crop/zoom and alignment between the visible press and the transient. Then play the result and closing hold with the music tail.

For an interactive player, pause/seek should stop the old scheduled sounds and restart from the new offset without doubled music/clicks; supplied voice should use that same offset. For deterministic export, render each sound event once from the shared timeline. Reuse the project's renderer/audio system; an extra player or separate effects package is not a required deliverable.
