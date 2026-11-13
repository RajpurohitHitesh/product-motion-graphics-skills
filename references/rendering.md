# Rendering and preview workflow

## Check the environment first

This skill is a production workflow, not a bundled rendering application. Inspect the target project's tools and reuse an existing renderer if suitable. For code-based motion graphics, Remotion is a practical option when Node, its compatible dependencies, and a render-capable browser are available. FFmpeg/ffprobe are useful for media inspection and independent output checks.

In an existing Remotion project, inspect its installed version, package manifest, entry point, compositions, and scripts. In a fresh output project, follow the current official setup documentation and keep compatible Remotion package versions aligned. Do not install a guessed stack in the skill library itself. Check the actual CLI help before relying on flags that differ by installed version.

Relevant official references, checked while authoring on 2026-11-14:

- [Remotion core model and composition properties](https://www.remotion.dev/docs/idea)
- [Rendering](https://www.remotion.dev/docs/render)
- [Render CLI](https://www.remotion.dev/docs/cli/render)
- [Still CLI](https://www.remotion.dev/docs/cli/still)
- [Audio component](https://www.remotion.dev/docs/media/audio)

If execution is unavailable, provide an honestly labeled storyboard and editable source. Explain which renderer/audio dependency remains necessary. Do not imply a playable MP4 was made unless it exists and can be inspected.

## Build around the chosen style

Wait for the explicit style selection described in [the main skill](../SKILL.md). Read only its style guide and any relevant learned techniques. In the output project, keep assets local and reference them through the renderer's supported media system. Preserve the original files.

Drive animations from frame/time values. At 30 fps, 30 seconds is 900 frames; frames run from 0 to 899. Derive durations from actual narration and the brief rather than scattering timing constants across components. For Remotion, register compositions with explicit `width`, `height`, `fps`, and `durationInFrames`. Use the media components supported by the installed version.

Keep text, product assets, palette, scene timing, and voice paths parameterized so feedback can be applied to the same project. Load fonts and images before rendering and use deterministic effects.

## Preview

Create a dedicated 6–8 second preview composition (or the full video if shorter) using the same product assets, style, typography, and voice identity as the intended final. Show a hook/product, a representative transition, and a benefit rather than an unrelated generic animation.

Use the final 1080 × 1920 layout with a 0.5 output scale to produce 540 × 960. A 6-second preview at 30 fps has 180 frames. Include the actual female narration sample when available. If the required audio is missing, identify the preview as silent and keep voiceover pending.

For an output project whose actual entry point and composition IDs match these examples, run from that project's root:

```sh
npx remotion render src/index.ts ProductShortPreview out/preview.mp4 --scale=0.5 --codec=h264 --audio-codec=aac --pixel-format=yuv420p
npx remotion still src/index.ts ProductShort out/storyboard-hook.png --frame=30
```

These IDs and paths are examples, not files bundled with this skill. Adjust to the real project. Render benefit and CTA stills at their actual scene frames too. A storyboard-only fallback is not a completed animated preview.

Show the playable file and describe which style and voice source it uses. Take feedback into the same project. Respect a requested preview/review stop; do not invent an extra approval gate when full production is already authorized.

## Final export and checks

Export the requested complete video. For the same example project:

```sh
npx remotion render src/index.ts ProductShort out/final.mp4 --codec=h264 --audio-codec=aac --pixel-format=yuv420p
```

Run the bundled checker by resolving its absolute path from this skill's location. `PRODUCT_MOTION_SKILL_DIR` below means that resolved folder; set it to the real location before running:

```sh
python3 "$PRODUCT_MOTION_SKILL_DIR/scripts/check_video.py" out/preview.mp4 --preview --duration 6
python3 "$PRODUCT_MOTION_SKILL_DIR/scripts/check_video.py" out/final.mp4 --duration 30
```

Use the actual expected durations, not necessarily 6 and 30. Pass `--fps 60` only if the brief intentionally changed the frame rate. For a clearly disclosed silent visual preview, the preview command may include `--allow-silent`; this option is rejected for final-video validation.

The helper requires `ffprobe` on PATH. It checks dimensions, square pixels, rotation, frame rate, duration, MP4 container, video codec/pixel format, and required audio codec. It does **not** assess whether an audio stream contains female speech, whether it is silent, whether claims are correct, or whether the preview looks good. Missing ffprobe is an unrun check, not a pass.

Watch the hook, transitions, captions, product details, and ending. Listen to the narration and music together. Verify no missing fonts/assets, clipped words, flicker, unreadable UI, or altered product details. Check caption sync against the real voice. Keep final export pending when required narration is unavailable.

Deliver files that exist: final MP4, playable preview, editable source, clean narration, and caption file as produced. Include the selected style, actual resolution/duration, and material limitations in a short handoff. Publishing/uploading requires a user request.
