# Headings and supporting text

Use with the selected style to design the complete text hierarchy: opening title, feature/step heading, label, supporting explanation, metric, captions and closing line. These are distinct roles; a scene needs only the roles that help it. Keep actual screenshot text unchanged. Source techniques come from the [three owner-supplied prompts](source-prompts/PROVENANCE.md); vertical sizes and product examples below are new adaptation choices, not measurements of their landscape canvases.

## What the references contribute

| Reference | Concrete hierarchy | Adaptation |
| --- | --- | --- |
| Creator Motion Graphics | Anton condensed statements; Instrument Serif italic accent; Inter topic labels, step chips and supporting lines; marked words and large numbers | A forceful short headline, one accent phrase, stable product context and quiet supporting explanation. Mainly 6/8; shorter bridges in 4/10. |
| Clean Tech | Inter Tight 800 headline, 500–700 card text; JetBrains Mono functional labels; masked word rise and one blue emphasis pill | Clear statement → named feature/relationship → readable supporting detail. Mainly 1/3/5/7, optional light 6. |
| Software Walkthrough | DM Sans 700 two-line task title; DM Mono eyebrow and metadata; numbered step pill; bold action label, muted supporting text and final checked lower third | Task title → current step → actual control/action → evidenced result. Mainly 2/3 and bounded workflow beats in 1/4/10. |

Use brand-approved fonts first. These reference families are optional implementation examples; choose available, licensed faces with complete glyphs for the output language. Preserve hierarchy when substituting fonts. Hindi requires proper shaping, readable weights, room for matras and a meaningful phrase rhythm; Latin all-caps/tracking does not transfer to it.

## Text roles and vertical scale

Starting sizes at **1080 × 1920**, adjusted to actual font metrics, copy and source layout:

| Role | Purpose | Starting treatment |
| --- | --- | --- |
| Eyebrow/topic | Small context such as “AMEZPRICE GUIDE” | 32–40px, medium/semibold; optional restrained tracking for Latin labels |
| Opening headline | The viewer's task or supported benefit | 80–116px, bold, usually 2–6 words across one or two deliberately broken lines |
| Feature/chapter heading | Name the current concept | 60–80px, semibold/bold, shorter than the spoken explanation |
| Step/action label | Tell the viewer what to do now | 48–60px, medium/semibold, with a small number badge when useful |
| Supporting line | Explain the meaning or next consequence | 44–56px, regular/medium, one concise line or two short lines |
| Caption | Carry the spoken phrase accessibly | 46–58px, readable contrast, at most two lines |
| Metric | Emphasize an exact supplied number | 110–160px where space permits; keep currency/unit/context readable alongside |

Kinetic/bold may enlarge one short keyword further; teaching/minimal can reduce dominance to protect the real UI. Critical instructions must not be demoted to tiny eyebrow text. Keep a consistent size/weight relationship across shots instead of choosing arbitrary new typography each time.

Measure using the loaded final font, wrap at semantic boundaries, then measure the full text box including highlight padding and script marks. Rephrase long headings or adjust the line break before shrinking them. Keep currency with its number and units with their values. Start around 1.05–1.15 line height for large Latin headings and allow more for complex scripts, then inspect the real glyph bounds. Do not crop diacritics with a reveal mask.

## Write for the viewer

Write the exact on-screen copy before animation. The heading states the task/meaning, the supporting line adds one useful explanation, and narration carries the longer guidance. A UI label alone is often too vague as the video heading. Examples for the verified AmezPrice context:

| Beat | Heading | Useful support |
| --- | --- | --- |
| Search | “Find your product” | “Search by name or brand” |
| History | “Read the price history” | “Compare recorded low, average and high” |
| Alert input | “Choose your target price” | “Get an alert at this price or lower” |
| Fixed-target removal | “Remove the fixed target” | “Enabled channels keep price updates on” |
| Complete alert shutdown | “Turn product alerts off” | Use the actual product-page or enabled-channel action |
| Amazon share | “Check it from Amazon” | “Share → AmezPrice” |

Created headings and supporting copy default to English, including when the user chats in Hinglish. Use Hindi/Hinglish on-screen copy only when explicitly requested for that output. For explicitly requested Hindi text, adapt the same meanings naturally, for example “अपना target price चुनें” and “इस कीमत या उससे कम पर alert”. A separately requested Hindi voiceover does not automatically translate English headings. Do not add a second text language unless requested. Avoid personal activity logs, generic hype, unsupported promises, or repeating the whole narration in every heading.

## Composition and timing

- A useful opening can have a small eyebrow, a strong two-line task title and one optional metadata pill. Include a step count or time estimate only when it matches the actual video/task. Do not copy the reference's “4 steps / about a minute” into unrelated content.
- Give the hero, headline and caption separate space. Keep a stable alignment edge and deliberate gap between title and support. For a vertical layout, stack roles above/below the hero; do not transplant a landscape split at tiny scale.
- Keep topic/step chrome in screen space while the screenshot camera moves. Attach a feature label or pointer to source space only when it identifies an actual UI element. Reserve space before animating either.
- Enter the title, let one keyword accent settle, then reveal supporting text. Clean Tech uses masked rises and a pill; Creator uses controlled slam/swipe; Walkthrough uses a clear task title followed by persistent current-step chrome. Text stays still for reading after its entrance.
- A step label changes when the actual next step begins. Keep its container stable in position and width where practical. Outcome text appears only when the supported result is visible. A quiet closing line can remain with the final product view.
- Treat headline and captions as separate semantic roles; merge them when they repeat the same words in the same area. Use one emphasized word/phrase per beat. Supporting text, every label and every caption word do not all need independent punch effects.

## Adaptation for all ten styles

| Style | Text pattern |
| --- | --- |
| 1 Feature | Short meaning-led heading + one explanatory callout; steady source metrics |
| 2 How-To | Task title + current numbered verb/action + exact control label + short result |
| 3 SaaS | Outcome-led opener + named feature + input/result labels; concise product benefit |
| 4 Layered App | Short hero headline + one supporting feature label during the card handoff |
| 5 Minimal | One restrained headline + optional quiet supporting line; generous empty space |
| 6 Kinetic | Designed phrase groups + one marked keyword; small stable product identifier |
| 7 Infographic | Claim/question heading + relationship labels + exact metric and unit |
| 8 Bold | Short forceful hook + marked benefit + readable real offer/result terms |
| 9 Cinematic | Restrained reveal title + sparse technical callout + quiet brand/CTA |
| 10 Dark AI | Brief kinetic bridge + real input/result labels + supported outcome title |

## Production handoff and checks

In each relevant shot record the exact role/copy, font token, size/weight, line breaks, alignment, box, emphasized words, screen/source space and entrance/exit times. Keep these parameterized as reusable Title, StepPill, FeatureLabel, SupportingLine, Metric and Closing components rather than drawing unrelated text styles per shot. Store the chosen system in the brief and reuse it for a requested [cover](thumbnails.md).

Inspect the opening, a dense feature/step and the ending at full resolution and phone-preview size. Check final-font loading, line wraps, matra/diacritic clearance, highlight contrast, units, caption/step collisions and readable holds. A detailed heading plan is not evidence of a finished video; verify the actual typography in the selected style's playable preview.
