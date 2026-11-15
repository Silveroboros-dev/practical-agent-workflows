# Style & Taste Resolutions v3

This document describes one optional editorial-gallery direction. It is a taste reference, not a universal brand book: adapt it to the audience, medium, and project requirements.

## Contents

- Canonical response frame
- Impression pattern
- Rare differentiators
- Core feeling and anti-taste
- Timeless principles
- Translation tokens
- Medium guidance
- Image generation
- Reference points
- Worked critique example

## Canonical Response Frame

Use this as the default output structure for critiques, redesign briefs, and art direction:

- `Direction`: the first-read impression and the main art-direction move.
- `Keep`: the taste principles, tokens, or interaction habits to preserve.
- `Avoid`: the concrete drift risks for this task.
- `Prompt language`: reusable wording for image prompts, visual briefs, or implementation notes when helpful.

Other sections in this document are reference material. This frame is the output shape.

## Impression Pattern

For any project, define the expected surface and the deeper discovery:

1. The audience arrives expecting a conventional version of the subject.
2. The surface feels calm, sparse, and highly composed.
3. Interaction or closer reading opens unexpected depth and structure.
4. The audience leaves sensing one authored intelligence behind the whole system.

That arc matters as much as any color or font choice.

Reference example, research archive:

1. A visitor expects a conventional document index.
2. The first view is calm, sparse, and highly composed.
3. On interaction, annotations reveal relationships between separate fields.
4. The visitor sees a coherent argument through the collection.

This is one example of the pattern, not a rule for every client, deck, or product.

## Rare Differentiators

These are the parts that make the taste specific rather than generically "high-end."

- `Treasure hunt`, not funnel.
- `Gallery-like but non-homogeneous`, not a polished product landing page.
- `Netsuke energy`: intricate craft revealed at close range, not loud ornament visible from far away.
- `Unexpected modality`: the interaction logic itself should help express the mind behind the work.
- `Interdisciplinary credibility`: different domains should feel authored together, not stitched together from separate aesthetics.

If these five qualities disappear, the style has drifted.

## Core Feeling

The work should feel:

- dark, editorial, and composed
- intelligent without needing to advertise intelligence
- authored rather than assembled from templates
- spacious at first glance and dense on closer inspection
- quietly luxurious without becoming glossy, fashion-forward, or expensive-looking in a shallow way
- serious enough for institutional finance and philosophy, but alive enough for AI and systems thinking

Useful shorthand:

- gallery, not dashboard
- treasure hunt, not feature funnel
- quiet authority, not performance
- crafted asymmetry, not sterile symmetry
- intellectual depth, not startup cleverness

### Luxury Distinction

Good luxury means material restraint, exact spacing, tactile surfaces, and intellectual structure.

Bad luxury means glossy shorthand: banking-premium UI, fashion moodboard drama, gold-on-black excess, or expensive-looking surfaces without substance.

## Anti-Taste Rules

Avoid these by default:

- fake corporate polish
- gamer aesthetics
- cyberpunk neon
- purple-on-black AI cliches
- generic startup gradients and blob language
- loud "premium" UI that feels like a bank ad or luxury-commerce campaign
- gimmicky motion
- over-explained visual metaphors
- overpacked homepages that reveal everything immediately
- moodboard luxury without intellectual structure underneath it

If forced to choose, prefer restraint over spectacle.

## Timeless Principles

This section is the durable part. It should survive even if the specific fonts, framework, or color codes change later.

### Atmosphere

- dark charcoal base
- soft white and muted gray text
- warm brass or archival-warm accents
- faint radial light used as atmosphere, never as a special effect
- tactile surfaces that suggest smoke, paper, glass, metal, stone, or annotation

### Composition

- slightly asymmetric layouts are welcome
- whitespace should breathe
- sections should feel curated, almost room-like
- hierarchy should come from composition and rhythm, not from large component libraries
- avoid turning every content block into the same card
- important elements should sometimes stand alone with visible air around them

### Interaction Philosophy

- interaction should reveal structure, not merely decorate it
- surprise should come from organization and unfolding depth
- clicks should reward curiosity
- motion should guide attention like a camera move or curatorial gesture
- conceptual persistence matters more than novelty for novelty's sake

### Shape Language

- soft corners, not bubbly corners
- medallions, sigils, small circular markers, and restrained badges are welcome
- borders should be thin and whisper-light
- ornament should feel etched, not inflated

### Tone of Finish

- elegant but not glossy
- refined but not fragile
- serious but not solemn
- premium but not performatively premium

## Translation Tokens

These are executable specifics. They are useful defaults, not eternal laws.

### Typography

Direction:

- Headings: light humanist or quiet display sans.
- Body: contemporary grotesk, calm and highly readable.
- Labels: tiny uppercase whisper labels with restrained tracking.

Approved fallback families:

- Avenir Next
- Geist
- Inter
- Sohne
- Neue Haas Grotesk
- Helvetica Neue
- IBM Plex Sans
- IBM Plex Sans Condensed, only when a compact editorial label or diagram voice is useful

Example typography translation:

- Display / heading direction: `"Avenir Next", "Helvetica Neue", "Segoe UI", sans-serif`
- Body / system direction: `"Geist Variable", sans-serif`

What matters more than the exact stack:

- headings should feel light, airy, and controlled
- body text should feel clear, modern, and quiet
- micro-labels should be uppercase, tracked out, and understated
- use line length, spacing, and weight for tension before theatrical font choices

Avoid:

- sci-fi geometric faces
- playful rounded app fonts
- ornate luxury serifs as a default
- defaulting to generic Inter-only startup sameness when the project needs an authored voice

### Color System

Example neutral color values:

- dark background: `oklch(0.128 0 0)`
- light foreground: `oklch(0.93 0 0)`
- dark card: `oklch(0.158 0 0)`
- dark border: `oklch(1 0 0 / 6%)`
- muted text: `oklch(0.62 0 0)`

Signature warm accent:

- brass accent: `#b8a27d`
- brighter hover brass: `#d3c09a`
- paper / artifact tone: `#d7cfbf`

Color behavior:

- keep the UI mostly neutral
- use the brass tone repeatedly but sparingly
- allow category colors in data layers, not across the whole surface

### Surface Treatment

- translucent dark surfaces
- low-opacity borders
- light backdrop blur, usually `2px` to `3px`
- soft black shadows instead of colored glows
- faint radial light in the background

The correct feel is smoked glass over a dark room, not consumer glassmorphism.

### Motion

- calm fades, lifts, and pans
- transition durations generally around `200ms` to `700ms`
- `easeOut` and `easeInOut`

Avoid:

- bounce
- toy-like springiness
- exaggerated parallax
- idle animation that begs for attention

## Medium Guidance

### Web and UI

- Start from mood and composition, not components.
- Define one warm signature accent and use it repeatedly.
- Keep the neutral field dominant.
- Do not flatten everything into identical cards.
- Use one strong interaction idea instead of many weak flourishes.
- On mobile, simplify the structure instead of shrinking a desktop composition.
- Preserve the impression arc: calm surface first, deeper structure on interaction.

### Decks, Diagrams, and Documents

- Slides should feel like curated exhibits, not consultant templates.
- Diagrams should use a limited palette and generous spacing.
- Reports should privilege rhythm, hierarchy, and margin space.
- Charts should be quiet by default, with emphasis added surgically.
- Labels and annotations should feel editorial and deliberate, not software-default.

Across media:

- the page should feel curated before it feels feature-rich
- the hierarchy should feel editorial rather than corporate
- the visual language should imply serious thinking rather than announce it
- the artifacts should feel selected, annotated, and placed, not mass-produced
- images across a series should feel like one publication mind, not a rotating moodboard

## Guidance for Image Generation

This section is deliberately strict. The goal is to prevent drift into generic "dark luxury" imagery.

### Positive Subject Anchors

Prefer images that include one or more of these:

- annotated diagrams
- archival paper, notebooks, schematics, or marked documents
- brass, graphite, smoke, stone, paper, glass, and matte metal
- geometric structures, maps, trees, matrices, grids, ledgers, or conceptual charts
- editorial still lifes that imply thought, systems, or inquiry
- quiet European interiors, desks, studies, galleries, libraries, or institutional spaces
- artifacts that suggest philosophy, mathematics, finance, governance, or AI without becoming literal clip-art
- recurring conceptual motifs across a series, so separate images still feel authored by the same intelligence

### Mood Anchors

Use phrases like:

- dark editorial gallery
- charcoal-black atmosphere
- warm brass accents
- archival restraint
- quiet authority
- authored asymmetry
- intellectual seriousness
- tactile materials
- curated depth
- calm surface, hidden complexity

### Composition Anchors

Ask for:

- sparse first read
- one clear focal object
- asymmetry with balance
- visible negative space
- layered depth rather than clutter
- suggestion of discovery or unfolding structure

### Negative Anchors

Avoid:

- cyberpunk
- neon palettes
- glossy corporate advertising
- startup hero illustration language
- generic AI swirls
- floating holograms
- bright synthetic gradients
- plastic 3D blobs
- overdesigned "luxury"
- sci-fi control room aesthetics
- gamer desk aesthetics
- visual noise pretending to be sophistication

### Short Reusable Image Prompt

> Dark editorial-gallery aesthetic with charcoal-black atmosphere, warm brass accents, archival paper and matte metal details, soft radial light, authored asymmetry, visible negative space, and a sense of hidden structure. Intellectual, restrained, tactile, and quietly authoritative. No cyberpunk, no startup gloss, no purple neon, no generic AI swirls.

### Expanded Reusable Image Prompt

> Create an image that feels like a curated intellectual artifact rather than a marketing visual. Use a dark editorial-gallery atmosphere with charcoal-black neutrals, off-white highlights, warm brass accents, matte metal, paper, smoke, stone, or smoked-glass textures, and a composed asymmetric layout with generous negative space. The image should suggest systems thinking, inquiry, or interdisciplinary depth through diagrams, annotations, ledgers, matrices, conceptual maps, or archival objects. It should feel calm on first glance and deep on closer inspection. Avoid cyberpunk, glossy corporate polish, startup gradients, gamer aesthetics, generic AI iconography, and any loud futuristic cliches.

## Worked Critique Example

Scenario: a dark homepage uses a purple AI orb, a centered hero funnel, three identical feature cards, and glossy gold highlights.

`Direction`

Move from "dark AI startup" to "curated intellectual artifact." Keep the dark field, but make the first screen quieter and more editorial: one focal object, one warm brass accent, more negative space, and an interaction that reveals structure rather than pushing users through a funnel.

`Keep`

- dark neutral base
- technical seriousness
- one clear focal area
- restrained accent color

`Avoid`

- purple orb as generic AI shorthand
- identical cards that flatten the work into SaaS features
- glossy gold that reads as fake luxury
- motion that only decorates instead of revealing structure

`Prompt language`

Dark editorial-gallery interface with charcoal-black atmosphere, warm brass accent used sparingly, archival diagram details, authored asymmetry, visible negative space, and one interaction that reveals hidden structure. Avoid cyberpunk, purple AI glow, startup gradient hero language, glossy premium banking UI, and generic neural-network imagery.

## Final Resolution

The style should always feel:

- thoughtful before flashy
- composed before loud
- structured before ornamental
- rich in implication rather than crowded with signals
- elegant enough for philosophy, rigorous enough for mathematics, credible enough for finance, and alive enough for AI
