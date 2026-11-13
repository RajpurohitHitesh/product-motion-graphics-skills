# Product production rules

## Brief and defaults

Use [the brief template](../templates/product-brief.json) for each output project. Keep user assets and generated deliverables outside the reusable skill folder. A useful project layout is `assets/`, `audio/`, `src/`, `out/`, and a working `brief.json`; adapt to an existing project instead of replacing its structure.

Default final canvas is **1080 × 1920, 9:16, 30 fps**. Default story length is 30 seconds, not a platform requirement. For YouTube Shorts, keep the requested duration within the currently supported limit; as checked on 2026-11-14, [YouTube documents up to three minutes for square or vertical uploads](https://support.google.com/youtube/answer/15424877?hl=en). Check the current rule again when a longer or boundary-length video is requested. Do not change duration just to fill the limit.

## Practical layout for this skill

These are adjustable design guides, not official YouTube safe-area specifications. The app's controls, description, and device layout vary.

- Start with left margin 90px, right margin 180px, top margin 180px, and bottom margin 330px on a 1080 × 1920 canvas for essential text, logos, and CTA. Decorative backgrounds can bleed to the edge.
- Keep meaningful product details away from the right control stack. Position captions within the usable area and reserve their space before placing other copy.
- Useful starting sizes: headlines 80–116px, supporting text 44–56px, captions 46–58px. Adjust for font, language, copy length, and actual phone readability.
- Prefer one short headline and one supporting idea at a time. Use at most two caption lines; segment speech into phrases instead of filling the screen with a paragraph.
- At 540 × 960 preview scale, evaluate text and composition at half these pixel values. Watch at phone size, not only enlarged on a desktop.

## Asset modes

### Images only

Inspect every image before planning its use. Identify the actual product, resolution, aspect ratio, logo, packaging text, available views, and existing background. Preserve the source files.

Create movement through deliberate crop changes, pan/zoom, masks, layered backgrounds, annotated details, or cutouts when suitable tooling is available. Use `contain` when full shape or packaging text matters; crop only when the story calls for a verified detail. Do not stretch photos. Avoid zoom beyond usable source detail.

A single photo supports 2D camera movement, not an accurate invented view of an unseen side. Generative image-to-video is optional and requires an available model; inspect its result for changed labels, dimensions, or product identity before using it.

### Clips only

Inspect playback and metadata. Select relevant moments, respect orientation, and use crop anchors that retain the product. Preserve an intentional before/action/after sequence. Use original clip audio when useful and lower it under the female narration. Do not silently retain someone else's voice as the requested female voiceover.

### Mixed inputs

Combine genuine action footage with still hero views and graphics. Match color treatment and perceived product scale. Use a repeated anchor, shape, or crop to bridge assets instead of masking every mismatch with a flashy transition.

### Reference versus source

Record each asset's role as `video-asset`, `style-reference`, or `both` in the working brief. Use links for style study when that is the user's intent. A reference video is not automatically source footage for the final commercial. If only an image of an unknown product is available, ask what it is and what benefits are approved rather than inventing them.

## Product story and factual integrity

Plan a hook, a recognizable product, a few supported benefits, and one action. The style guides show adaptable 30-second structures, not mandatory shot grids.

- Derive specifications, offers, savings, compatibility, and performance claims from supplied or verified product information. Mark uncertain facts in the brief and omit them from final claims until resolved.
- Use real interfaces for real feature claims. Clearly identify illustrative mockups or sample data.
- Do not add invented testimonials, certification marks, stock scarcity, discounts, or numerical charts.
- Retain the product's actual form, colors, and identity. Background treatment can adapt to the style without changing the product itself.

## Shared motion rules

Use a consistent easing family, type hierarchy, and transition vocabulary from the selected style. Convert seconds to integer frames using the actual fps. Time visible actions to the recorded narration; music can add rhythm without controlling every shot.

In code renderers, drive animation from the composition timeline and deterministic inputs. Wall-clock timers, unseeded random particles, network-loaded fonts, and unfinished image loads can produce inconsistent frames. Resolve media and fonts before a render, and clamp interpolated values where necessary.

Before delivery, inspect the opening, transitions, densest caption, product detail, and final CTA. Listen for clipped words, abrupt music cuts, and speech masked by effects. Technical checks and visual/audio review serve different purposes.
