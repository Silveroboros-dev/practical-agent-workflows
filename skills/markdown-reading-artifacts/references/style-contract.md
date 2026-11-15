# Editorial HTML Style Contract

Use this contract for Markdown-derived HTML documents.

## Dark Tokens

- `--bg: #0f0f0f`
- `--panel: rgba(27, 27, 26, 0.9)`
- `--panel-2: rgba(18, 18, 17, 0.94)`
- `--paper: #d7cfbf`
- `--text: #ece9e2`
- `--muted: #a4a09a`
- `--accent: #b8a27d`
- `--accent-2: #d3c09a`

## Light Tokens

- `--bg: #f3efe6`
- `--panel: rgba(255, 252, 244, 0.9)`
- `--panel-2: rgba(236, 230, 217, 0.95)`
- `--paper: #201d19`
- `--text: #292620`
- `--muted: #6f675c`
- `--accent: #8b6f43`
- `--accent-2: #5e4b2c`

## Layout

- Fixed TOC on desktop, hamburger TOC on mobile.
- Content max-width around 760px.
- H2/H3 collapsible sections open by default.
- Section rail must remain aligned. Do not use alternating `margin-left`, `padding-left`, or `nth-of-type` offsets for sections.
- Use small circular markers and thin dividers for artifact feel.

## Interaction

- Clicks should reveal structure: TOC, collapsible sections, copy buttons.
- Keep transitions calm and short.
- Print CSS must expand all sections and hide controls.

## Avoid

- cyan/purple startup palettes;
- cyberpunk or gamer styling;
- gradient blobs or decorative orbs;
- glossy luxury surfaces;
- section drift that harms scanning;
- external fonts, CSS, or JS.
