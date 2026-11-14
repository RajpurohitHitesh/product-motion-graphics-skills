# Motion craft across the ten product styles

Use after selecting the primary style, with that style's own guide. These techniques improve its execution; they do not replace its palette, pace, product, or purpose. Source mapping and access limits are in the [comparison study](video-studies/2026-11-14-craft-upgrade.md). The three full owner-supplied prompts are archived in [source prompts](source-prompts/PROVENANCE.md); load only a relevant example when implementation detail is needed.

## Choose a treatment

| Treatment | Strongest fit | Selective fit | Preserve |
| --- | --- | --- | --- |
| Creator Motion Graphics | 6 Kinetic, 8 Bold | Hook/CTA in 4 and 10; one number reveal in 7 | Condensed display hierarchy, one marked keyword, controlled punch, coherent graphic transitions |
| Clean Tech | 1 Feature, 3 SaaS, 5 Minimal, 7 Infographic; light variation in 6 | Card hierarchy in 2/4; technical annotation in 9; dark adaptation in 10 | Masked phrase reveals, one accent pill, whitespace, purposeful cards and connections |
| Software Walkthrough | 2 How-To, 3 SaaS | A bounded explanation in 1; a genuine action/result beat in 4/10 | Locate → act → see result, input typing, anchored spotlight, numbered task progress |

All ten share timing, focus discipline, sound-event mapping, vertical reflow, and cover planning. A physical-product reveal does not acquire a software window just because the walkthrough reference has one. Choose one main treatment and at most a useful secondary technique; do not concatenate three demos.

## Design beats before effects

For each meaningful beat record: actual source asset/state, spoken line, exact short headline, focus target, action/result evidence if relevant, transition, duration, and sounds. A tutorial beat may contain several supported action states; a sentence need not force a new shot. Give an explanation or outcome enough reading time before moving on.

Three to six meaningful visual layouts usually communicate more than repeated full-screenshot swaps: establish, focus, explain, input/action, result, closing. Reuse landmarks between related layouts. For longer tutorials, group steps into chapters rather than accelerating the voice or hiding prerequisites. Split into independent videos when the user permits it and each needs a different task outcome.

For a storyboard, use the same drawing/layout components as the final composition, with beat time, words, focus move, transition, and sound below each panel. A requested storyboard review is a stopping point. Otherwise the references' mandatory storyboard approval is not an additional production gate; follow the current brief and existing skill flow.

## One timeline for picture, type, and sound

Build a deterministic shot/event map in the output project. Reference times from one map rather than duplicating offsets in captions, animation, and audio code:

```json
{
  "id": "target-entry",
  "start": 12.0,
  "end": 16.5,
  "assetId": "actual-target-form",
  "spokenLine": "Enter your target, then select Set Alert.",
  "focus": {"sourceRect": [0.05, 0.52, 0.90, 0.10]},
  "events": [
    {"id": "focus", "at": 12.2, "kind": "focus", "sound": "soft-swell"},
    {"id": "type", "at": 12.7, "end": 13.6, "kind": "typing", "text": "62000", "sound": "keys"},
    {"id": "save", "at": 14.2, "kind": "tap", "sound": "click"},
    {"id": "result", "at": 14.5, "kind": "supported-result", "sound": "soft-chime"}
  ]
}
```

This is an illustrative authoring structure, not evidence that a product has this form or response time. Replace its asset, coordinates, input, times, and next state with the current evidence. Store source rectangles normalized to the actual image, and transform annotations with their source parent.

- With recorded narration and word timings, place key text/number landings on their spoken words; approximately one output frame is a useful alignment target. A camera can lead the named control by roughly 0.2–0.3 seconds when it helps orientation.
- Line-level timestamps can support approximate drafts. Length-weighted word interpolation is an estimate; inspect/adjust against the audio before claiming word sync. Do not require word timestamps for a prompt-only task or a music/SFX-only video.
- With voiceover coming later, mark timing as provisional and keep the voice track empty. Use the approved script to reserve time. Do not generate narration contrary to the user's instruction.
- Cut at idea boundaries, retain natural spoken phrases, and let the last meaningful result settle. The reference's last-word + 1.2 seconds is an optional tail, not a replacement for a requested duration cap.

## Typography and field typing

Use [the heading system](heading-system.md) for title, step/feature heading, supporting line, labels and metrics. Keep that designed hierarchy distinct from optional accurate speech captions; merge competing layers when they repeat the same words in the same area. Choose a font with real glyph support for the requested language; the reference's Latin-only display choices and all-caps rules do not transfer automatically to Hindi.

Masked rises suit Clean Tech; scale-settled emphasis suits Creator. Mark one word with a pill/swipe, keeping its text contrast readable throughout the reveal. Use the restrained version in teaching/minimal styles. Do not animate every caption word with a camera kick.

When showing input, focus the real field → place a caret → reveal characters → pause on the final value → show the supported submit/selection action. Match font, padding, currency sign, and final input to the source. Animate a separate text layer clipped inside the field; leave its border, icon, and surrounding UI intact. Use grapheme-aware progression for complex scripts. Preset selection is a tap, not invented manual typing.

## Focus and truthful action

Orient on the screen, approach one relevant control, act, and let the result become legible. Use one rounded spotlight, outline, or magnifier; dim context without losing navigation landmarks. Return to enough context before the next step. Stop camera drift while a user must read a graph or input.

Desktop recordings can use an eased cursor path and a brief pressed state; mobile screenshots use a touch cue. Click feedback should be prompt when genuine footage/state evidence supports it. The reference's 0.1-second feedback is an illustration, not a performance promise for the actual app. Never invent a toast, enabled toggle, notification, or delivery event to complete the story.

## Depth, camera, and transitions

Assign a visual reason to every move: entry, locate, compare, reveal, or confirm. Give cards consistent depth order, shadow direction, and scale. Settle them to a readable frontal pose before detailed information. Genuine screenshot text stays sharp; depth does not justify guessed interface content.

Use one or two transition families per video. Clean pushes, landmark match cuts, and a zoom into a relevant detail suit teaching; a small whip or punch may suit a bold hook. Restrict Creator's shake, flash, glitch, and light-leak stack to optional brief accents in energetic styles. Minimal, instructional, and data-reading beats retain steady holds.

Reflow the 1280 × 720 examples natively for 1080 × 1920. Stack headline, primary feature, and caption/step area; bring a secondary panel forward when needed instead of shrinking a landscape split. Keep every critical field readable at phone size. The source Clean Tech layout at 14.1s has a headline close to/behind the adjacent report card; resolve that overlap rather than copying it.

## Event-based sound design

Choose the background bed, music phrasing, speech mix and pointer choreography using [sound and cursor direction](sound-and-cursor.md). Store click-ripple origins at the activation's source position so they do not follow a departing cursor. Keep step chrome in screen space and actual target cues in the screenshot's transformed source space.

| Visible event | Starting sound choice | Limit |
| --- | --- | --- |
| Tap/click | Short, soft click | One per actual illustrated activation |
| Typing | Quiet key texture within the input interval | Ends with typing; no noise through a reading hold |
| Card/menu entry | Rounded pop | Smaller events remain subordinate |
| Focus move/push | Low, soft swell/whoosh | Do not mask a control name |
| Keyword pill/swipe | Restrained swipe/tick | Reserve stronger accents for a few key ideas |
| Numeric change | Soft tick when the shown value changes | Cap density; do not sound every frame |
| Supported saved/result state | Short resolving chime | Not a fake notification or delivery proof |

Music, SFX, and narration remain separate tracks. Use a lighter effects/music mix under supplied speech. No-voice means no generated speech, vocal samples, or sung lyrics. The examples' synthesized oscillator helper named `voice` is an instrument, not TTS. Exact gains and sound quality still need listening; source-code inspection cannot establish a finished mix.

## Preview and QA

Use the selected style's representative preview, not a generic sample. Inspect first frame, action boundaries, densest text, numeric landing, transition midpoint, result, and CTA at phone size. For a full video, a timestamped contact sheet at roughly 0.5–1 second intervals helps find collisions; play the relevant sections to verify continuous motion and listen to the actual mix too.

For code renderers, explicitly load the used font faces/weights with the target script, await `document.fonts.ready` and image decoding, then seek to the same time after seeking elsewhere and compare the frame. Do not rely on a player-specific ready flag alone. Seed noise/particles and keep all state derived from time; check effect events are not duplicated by seeking. A contact sheet is not playback; a valid media container is not proof of sound or visual quality.

Plan a deliberate first frame and cover candidate using [thumbnail guidance](thumbnails.md). Reuse the working composition. Deliver only requested variants and packages; keeping source for revisions does not require constructing an additional HTML player or another editable format.
