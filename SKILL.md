---
name: product-motion-graphics
description: Create vertical product motion graphics, feature explainers, and app tutorials from real images, clips, or screenshots using ten selectable styles. Support scripts/prompts, previews, final videos, and requested covers; improve the library from references. Use for product-focused videos rather than unrelated faceless stories.
---

# Product Motion Graphics

Create product-focused videos with a clear hook, a visible product, truthful benefits, and a useful call to action. Support physical products and digital products. Keep every style inside this skill; do not create a separate skill for each style.

For a user-facing overview, workflow diagram, requirements, and ready-to-copy prompt files, see [the usage guide](README.md). Read it when explaining how to use the skill; production routing remains below.

## Defaults

- Platform: YouTube Shorts, **1080 × 1920, 9:16**, 30 fps.
- Duration: 30 seconds unless specified; adapt the story to the requested length.
- Inputs: images only, clips only, screenshots, or a mixture; accept brand assets and audio too.
- Voice: natural, adult female delivery. Prefer a supplied human recording; otherwise use an available female TTS voice and identify it as AI-generated. See [voiceover](references/voiceover.md).
- Language: keep skill documentation and example prompts in English. Default video scripts, narration, and captions to English; use another language for a specific video only when the user explicitly requests it.
- Output: playable video preview, then the requested final MP4 and editable source.
- Style: **no default selection**. Never infer style selection from supplied assets or a reference link.

These are production preferences, not claims that YouTube requires this exact resolution, frame rate, or duration.

Explicit current instructions override defaults, including language, voice and deliverables. If the user will add ElevenLabs narration later, prepare the script and timing markers without generating speech; music/SFX-only output is valid when requested. Do not create additional player exports or editable formats merely because a reference includes them.

## 1. Decide what the user is asking for

- **New product video:** follow the style selection and production flow below.
- **Prompt or script only:** inspect supplied assets and write the requested plan/prompt with filename-to-scene mapping; do not render a video or build an editable project unless asked.
- **Product brand setup:** follow [brand setup](references/brand-setup.md) to create or update reusable context in the output project. Setup alone does not select a video style or authorize a preview.
- **Revise the current video:** retain its selected style unless the user requests a change. Show a revised preview.
- **Learn from references:** follow [reference learning](references/reference-learning.md). A learning request alone does not require a style-selection question or video render.
- **Learn and make a video:** learn first, update the menu, then ask the user to select a style before previewing.

Read only the chosen style and the references needed for the current task. Do not load every style guide into every video request.

Before planning or animating a product video, read the output project's `brand.md` and `MOTION.md` when present. Reuse established assets and preferences; current explicit user instructions take precedence. Missing profiles do not block work when the supplied assets and brief establish the necessary facts. See [brand setup](references/brand-setup.md) when profiles are requested or need updating.

For **Amezprice**, read [the product preference profile](references/products/amezprice.md) before presenting style choices. It records the owner's highest-priority reference and recommended visual direction. A preferred reference is a recommendation for the selection prompt, not permission to skip the explicit style-selection gate.

For screenshot-based feature explanations, recommend **1 — Screenshot / Feature Explainer**; for repeatable how-to instructions, recommend **2 — Guided / How-To Tutorial**. Follow [screenshot production](references/screenshot-videos.md) after the user selects. Style 4 remains a recommendation for AmezPrice app promos; recommendations depend on the video's purpose.

## 2. Always ask for style selection for a new video

Read the current [style menu](styles/INDEX.md), including styles added later. Present its numbered choices with a short description in English unless the user explicitly requests another language. Ask:

> Which style would you like for this product video? Select a number or style name, and I will create a preview in that style.

For **each new video**, wait for the user's choice before generating its visual preview or choosing a style. If the request already names a style, show it as the proposed choice and ask the user to confirm; this explicit selection is the owner's preference. A previous video's choice does not automatically carry over to a new video. Recommendations are allowed, but recommendations, silence, reference links, or inferred product fit are not selections.

Offer all styles in the current menu. A custom or mixed style is possible when explicitly selected; ask which style leads and which secondary element to borrow. Do not force all styles into one video.

Before selection, you may inspect supplied assets, check runtime availability, and organize the brief. Do not make style-specific preview images, videos, or voice samples yet. This selection gate applies when using the skill to produce a video, not when editing the skill itself.

## 3. Prepare the product brief

After selection, read that style's guide and [production rules](references/production.md). Start from [product brief](templates/product-brief.json) in the **output project's** working directory; do not overwrite the reusable template.

Use [motion craft](references/motion-craft.md) for shot/event timing, field typing, focus choreography, sound and phone-size QA. Its three treatments map into the existing ten styles; read only the selected treatment's [archived source prompt](references/source-prompts/PROVENANCE.md) when helper code is needed. For a requested cover or a cover-ready opening, use [thumbnail guidance](references/thumbnails.md). Ready-to-copy adaptation prompts are in [style upgrades](prompts/style-upgrades.md).

Design exact title, step/feature heading, supporting line, labels, metric and caption roles using [the heading system](references/heading-system.md). Record their hierarchy, font tokens, line breaks and emphasis before animation. For a music/effects or interaction preview, use [sound and cursor direction](references/sound-and-cursor.md): choose a style-appropriate bed and coordinate pointer approach, press, ripple, actual result and sound on the same event map.

Record the product, verified benefits, audience, duration, CTA, selected style, assets, language, voice source, and output settings. Reuse details already provided. Ask only for missing essentials such as an unknown product or the actual human recording when a real human voice is required. Use the documented defaults for optional details.

Record the borrowed treatment, actual/estimated timing status, action and sound events, requested cover, and requested deliverables in the brief. Use one event map for picture and sound; keep optional archive players and publication copy out of the task unless useful and requested.

Treat style guides as a visual language with adaptable examples. Design the hook, scene grouping, layout, crops, and transitions around the actual assets and purpose. Retain the recognizable selected style and real product facts; preserve an approved repeat layout when requested. Tutorial action dependencies constrain scene order even when the presentation is creative.

Classify assets as either **to appear in the video** or **visual references**. A product photo can serve both purposes when intended. Preserve actual product proportions, logos, packaging, interface text, and approved claims. See the production rules for images, clips, and mixed inputs.

## 4. Make a preview after selection

Follow [rendering and preview](references/rendering.md) and [female voiceover](references/voiceover.md).

- Write a compact product story and voice script; use the selected style's pacing.
- Show the actual intended heading hierarchy and a representative music/click/typing mix in the playable preview when those elements are requested. Generic labels and an unreviewed sound score do not validate the finished treatment.
- Make a representative **6–8 second playable preview at 540 × 960**, or the full duration when the requested video is shorter. Include the product, characteristic typography/motion, a transition, and a natural female voice sample when audio is available.
- Show three representative storyboard stills for hook, benefit, and CTA when practical. Stills supplement the animated preview; they do not replace it.
- Identify the selected style, any learned variation used, voice type, and missing assets in a short note. Link actual generated files.
- If rendering or voice generation is unavailable, say exactly what could and could not be produced. A storyboard is a **storyboard**, code is **source**, and a silent preview is **silent**. Never label them as a rendered video with female voice.

Respect preview feedback. If only a preview was requested, stop after delivering it. If the user requested review before final export, wait for that review. If full production is already authorized, a second approval is not required merely because a preview exists.

## 5. Finish the requested video

Keep the selected style, narration, colors, and product depiction consistent. Export the requested final video at 1080 × 1920, with H.264 video and AAC audio in MP4 unless explicitly changed. Include captions aligned with the recorded speech. Do not silently omit female narration; report it as pending if the required audio is unavailable.

Run [check_video.py](scripts/check_video.py) against the rendered files using the commands in the rendering guide. Also watch and listen to representative sections; metadata cannot prove voice quality, synchronization, visual accuracy, or readability.

Review a timestamped contact sheet and action/transition boundary frames for collisions and source-aligned highlights. Export a requested cover from a settled composition using the same assets; do not render the complete video again just to get a thumbnail.

Deliver final MP4, preview, editable project, and captions/voiceover files when produced. State any unresolved limitation. Do not upload to YouTube unless asked.

## Improving this skill

When the user supplies video links to improve the library, use [reference learning](references/reference-learning.md). Improve a matching style with evidenced, reusable techniques; create a new style folder when the visual language is genuinely different. Update [the menu](styles/INDEX.md) so new styles appear in future selections. Do not invent observations from a link that could not be watched.

Previously studied videos and their access/verification limits are listed in [video studies](references/video-studies/INDEX.md). Read an individual study only when its variation is relevant; visual storyboard review does not establish audio, easing, or exact transition timing.

## Use in Claude

This is a portable skill folder. For Claude Code discovery, place this entire folder at `.claude/skills/product-motion-graphics/` inside the target project, or `~/.claude/skills/product-motion-graphics/` for personal use. Then invoke `/product-motion-graphics` or describe a matching task. Keep the styles, references, templates, and scripts together.

The skill supplies instructions, a video-checking helper and three archived HTML/canvas reference prompts. These examples are not a configured production renderer, TTS service, credentials or the user's product assets. Check the target environment before promising a rendered preview or voiceover. In environments without video execution, prepare source and clearly labeled storyboard material until rendering is available. See [Claude skills documentation](https://code.claude.com/docs/en/skills).
