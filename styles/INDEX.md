# Product video style menu

Use this file as the source of choices whenever the skill asks for a style. Append new styles here after creating their guides. Keep existing numbers stable unless the owner explicitly requests a new order; then update numbered references throughout the skill.

Human-facing examples are in the [usage guide](../README.md). Keep its style table and example prompt numbers in sync when adding or reordering choices.

| Choice | Style | Visual character | Useful for | Guide |
| --- | --- | --- | --- | --- |
| 1 | Screenshot / Feature Explainer | Real UI, Clean Tech feature focus, anchored callouts and metric explanation | Explain an app feature, graph, score, or supported use case | [Feature Explainer](screenshot-feature-explainer/STYLE.md) |
| 2 | Guided / How-To Tutorial | Software Walkthrough steps, real input typing, accurate taps and supported results | Teach a repeatable app task from screenshots or recordings | [How-To Tutorial](guided-how-to/STYLE.md) |
| 3 | SaaS / Product Demo | Focused walkthrough, Clean Tech input/result cards; optional depth and device showcase | Apps, websites, digital tools, software | [SaaS](saas-product-demo/STYLE.md) |
| 4 | Layered / 3D App Showcase | Hero/support card hierarchy, readable depth and deliberate feature handoff | App promos; owner's priority direction for Amezprice | [Layered App Showcase](layered-app-showcase/STYLE.md) |
| 5 | Minimal / Apple-inspired | Spacious product framing, restrained Clean Tech masked type and quiet accents | Premium products, packaging, elegant launches | [Minimal](minimal-apple/STYLE.md) |
| 6 | Kinetic Typography | Creator Motion Graphics or Clean Tech kinetic treatment, timed keyword emphasis | Benefit-led promos, slogans, energetic launches | [Kinetic](kinetic-typography/STYLE.md) |
| 7 | Infographic / Explainer | Clean Tech causal diagrams, honest metric landings, clear relationships and units | Product mechanisms, specifications, explainers | [Explainer](infographic-explainer/STYLE.md) |
| 8 | Bold Social Media | Creator-style product hook, marked words, controlled punch and readable payoff | Attention-grabbing Shorts, offers, launches | [Bold](bold-social-media/STYLE.md) |
| 9 | Cinematic / Futuristic | Directional light, purposeful camera, scene-attached technical labels and material detail | Tech, gadgets, dramatic product reveals | [Cinematic](cinematic-futuristic/STYLE.md) |
| 10 | Dark / AI Product Launch | Dark stage, genuine typed input/result, restrained kinetic bridges and edge highlights | AI tools, coding products, creative software, feature launches | [Dark AI Launch](dark-ai-launch/STYLE.md) |

The user selects one style before preview generation. A custom combination is available by request, with an explicit primary style. These choices are visual approaches to **product videos**, not separate skills.

Suggested English menu wording:

> Which style would you like to use? 1 Screenshot Feature Explainer, 2 Guided How-To, 3 SaaS Demo, 4 Layered / 3D App Showcase, 5 Minimal, 6 Kinetic Typography, 7 Infographic Explainer, 8 Bold Social, 9 Cinematic, or 10 Dark AI Launch? Select a number or name, and I will create a preview.

Generate this wording from the current table so future styles are included too.

Variations remain inside their parent style. After the user selects a style, describe a relevant variation if useful; do not combine every variation automatically. See [reference batches](../references/video-studies/INDEX.md) for evidence and verification limits.

For AmezPrice, recommend by purpose: **1** for feature explanations, **2** for how-to instructions, and **4** for app promos using the owner's preferred visual reference. Still ask for style selection. Follow [the product profile](../references/products/amezprice.md) for reference priority and product evidence, and [screenshot production](../references/screenshot-videos.md) for screenshot-to-video work.

Styles 1 and 2 are owner-requested hybrids of existing families, authored for different teaching outcomes. They are not new reference-video observations and do not require mixing every style into one video.

All ten use [shared motion craft](../references/motion-craft.md) and distinct [cover recipes](../references/thumbnails.md). Creator Motion Graphics, Clean Tech and Software Walkthrough are mapped treatments within these choices, not additional numbered styles. See the [comparison and evidence limits](../references/video-studies/2026-11-14-craft-upgrade.md) and [three adaptation prompts](../prompts/style-upgrades.md).
