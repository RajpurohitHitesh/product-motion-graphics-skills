# Videos from app screenshots

Use this workflow for [Style 1 — Screenshot / Feature Explainer](../styles/screenshot-feature-explainer/STYLE.md) and [Style 2 — Guided / How-To Tutorial](../styles/guided-how-to/STYLE.md). It also supports relevant screenshot scenes in other selected styles. Use shared rendering, voice, and product-integrity rules; do not load unrelated style guides.

## Choose the teaching purpose

| User's goal | Recommend | Key result |
| --- | --- | --- |
| Explain a feature's meaning or benefit | 1 | Viewer understands the feature and a supported use case |
| Teach a repeatable app task | 2 | Viewer can follow the verified actions and recognize the result |
| Promote the app with visual breadth | 4 | Viewer recognizes the app and its supported benefits |
| General interface demo with an existing production approach | 3 | Clear action/result demo using that selected style |

Recommend the appropriate choice, then apply the main skill's explicit selection gate. A requested skill/library edit does not require selecting a style or generating a preview.

## Inspect and map the supplied screens

Inspect the actual files and record their source dimensions, what is visible, app/version consistency, and role. Use full-resolution owner-supplied assets for production; saved low-resolution YouTube storyboards establish context, not suitable final screenshots.

- **One screenshot:** a visible-feature explanation or one bounded verified instruction is possible. Hidden screens, controls, and results are not established.
- **Several screenshots:** establish sequence from the supplied order, a recording, documentation, or user confirmation. Do not guess navigation from attractive layouts alone.
- **Screenshots plus recording:** use the real recording for actions where it helps, then return to a screenshot/detail when it improves readability.

For AmezPrice, consult [the product profile](products/amezprice.md). Its promo supports attributed feature representations; current exact button labels/routes still need appropriate evidence. Distinguish source values from current live values and illustrative teaching data.

## Working scene plan

Use `purpose` in the output project's brief to record, for example, `feature-explainer`, `how-to`, or `product-promo`. Use its `screenshotPlan` list for the relevant scenes. Each scene should identify:

| Field | Meaning |
| --- | --- |
| `sourceFile` | Actual screenshot/clip path in the output project |
| `screenId` | Stable identifier used to link scenes |
| `visibleConcept` | What the scene can truthfully show |
| `focusTarget` | Source-relative box/point to crop or annotate, when needed |
| `spokenLine` | Explanation or instruction to align with actual narration |
| `action` and `actionEvidence` | For how-to: actual action and how its behavior/order was established |
| `nextScreenId` | Supported next/result scene, if relevant |
| `timing` | Scene timing derived from the recorded voice and reading load |

Omit fields that do not apply. Write the working plan in the output project; do not populate the reusable brief template with invented user screens or placeholder success states.

## Screenshot treatment

Use the [Software Walkthrough and Clean Tech adaptations](motion-craft.md) when they suit the selected style. Field typing should be clipped within the actual input; preset selection remains a tap. Highlight and cue geometry must follow the same source-to-output transform as the screenshot. A slight camera lead can locate a control before narration names it, followed by a stable reading/action hold.

Preserve original files, aspect ratio, UI labels, logos, data, and visual identity. Prefer a readable crop plus enough context to orient the viewer. Do not stretch a screenshot, invent missing screen content, or use generative redraws to alter the UI.

Represent highlights, arrows, callout labels, and tap cues as separate presentation layers. Store their coordinates relative to the original source image. Apply the screenshot's crop/scale/offset consistently to those layers, or place them in the same transformed parent, so a focus move does not detach a highlight from its control.

Keep magnified UI sharp within its usable resolution. If a control cannot be read from the source, obtain the necessary crop/export instead of inventing its text. A side label can repeat the exact real control name at a readable size.

Use restrained context dimming, a focus outline, or a small magnified region. Avoid multiple competing focus devices. Restore useful context between scenes; maintain a clear separation between UI labels, explanatory callouts, and speech captions.

## Creativity within the selected style

Adapt the hook, composition, crop sequence, callout design, and scene grouping to the actual screenshots and topic. The example timelines are not fixed templates. A new asset set can lead to a fresh story while the selected style stays recognizable.

For tutorials, required action order, control labels, and genuine results constrain the story. For feature explainers, choose a useful conceptual order without creating unsupported functionality. Preserve an approved layout when the user asks for consistent series formatting or an exact repeat.

## Preview and finish

Plan a [cover-ready feature/task composition](thumbnails.md) from an actual supplied screen or result. Use a clear task title or feature benefit rather than personal activity narration. Keep the active control visible outside captions and chapter/step chrome.

After user style selection, use the shared 6–8 second 540 × 960 preview flow with a representative complete explanation/step and actual female narration when available. Final delivery remains 1080 × 1920, 9:16 by default. Keep source, captions, and clean narration as produced.

Review at phone size: can the viewer read the real UI, identify the highlighted item, understand the spoken line, and recognize the supported next state? Check all cue positions after the final crop, real step order, actual result evidence, caption timing, screenshot consistency, and missing assets. Metadata checks cannot establish these properties.
