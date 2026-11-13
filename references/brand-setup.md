# Reusable product brand and motion context

Use when the user asks to set up or update their product brand for motion work. This is a mode of the product skill; it does not add a separate skill or a new visual style.

## Read before asking

Inspect the output project's existing `brand.md`, `MOTION.md`, supplied brand assets, and relevant project instructions. For AmezPrice, also read [the product profile](products/amezprice.md). Reuse information already established. Ask only for facts or assets necessary to resolve a real gap; optional details may remain pending.

Do not change the reusable skill's brand defaults for one client's project. Save these project-specific profiles in the output project, preserve existing unrelated content, and keep original media intact. Do not add credentials or private tokens to the profiles.

## What the profiles contain

| Output-project file | Store | Evidence boundary |
| --- | --- | --- |
| `brand.md` | Product name, intended audience, supported features/benefits with sources, tone, CTA, logo/media locations, and key product constraints. | Distinguish owner-approved facts, source-attributed representations, and unresolved claims. A promotional source does not verify live backend behavior or current prices. |
| `MOTION.md` | Supplied color tokens and fonts, logo treatment, preferred composition/type hierarchy, motion/transition preferences, voice/language/caption preferences, output defaults, and asset references. | Distinguish supplied exact tokens from approximate observations. Keep unconfirmed design proposals identifiable; do not report guessed hex values or easing as brand specifications. |

Profiles are reusable context, not a permanent video brief. Keep an individual video's hook, sequence, actual narration timing, selected style, and asset plan in that output project's working brief. A brand's preferred style is a recommendation; the user still selects/confirms each new video's style.

## Setup behavior

1. Reconcile supplied assets and existing profiles; identify contradictory or unverified details that matter to this job.
2. Write concise, sourced context using actual file locations. Retain useful existing choices unless the user changes them.
3. Record required unknowns as pending rather than inventing tokens, product facts, or a human recording.
4. Summarize what was saved and which details remain unresolved. Setup can finish without rendering a style preview.

The subsequent video workflow reads these profiles before scene design. Explicit current user instructions override stored preferences. Only persist a temporary per-video override when the user wants it to become a reusable brand preference.

## Optional project read-first snippet

For a user who wants the same context discoverable from their project's instruction file, provide this snippet for the project's `CLAUDE.md`. If asked to integrate it, preserve existing instructions and add only a scoped block; keep the file locations accurate to that project. Merely creating the skill documentation does not install this block anywhere.

```markdown
## Product motion context

For product-video work in this project, read ./brand.md and ./MOTION.md when
present before planning scenes or animating. Use them for established assets,
verified product facts and brand/motion preferences. The current user's explicit
instructions take precedence; mark unknown facts rather than inventing them.
Use the Product Motion Graphics skill's current style menu and ask the user to
select/confirm a style for each new video before creating its visual preview.
```

If profiles are absent, follow the skill's normal asset and brief intake. Do not claim a result follows a documented brand system until the necessary brand details have actually been established.

The user-facing setup prompt is in [brand-design-system](../prompts/brand-design-system.md).
