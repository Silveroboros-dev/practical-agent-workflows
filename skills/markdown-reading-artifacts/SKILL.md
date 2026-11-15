---
name: markdown-reading-artifacts
description: Convert Markdown source documents into self-contained HTML reading artifacts with dark or light themes, collapsible sections, a table of contents, code-copy controls, validation, and optional static portal bundles. Use when the Markdown must remain the content source of truth.
---

# Markdown Reading Artifacts

Render Markdown as a self-contained HTML reading document. The included style is a restrained editorial theme with aligned content rails, quiet borders, and a warm accent. Adapt the visual treatment if the user's project needs another style; preserve source content and semantic structure.

## Content contract

- Do not rewrite, summarize, or add substantive claims during conversion.
- Preserve headings, paragraphs, lists, quotations, tables, links, inline code, and fenced code where the renderer supports them.
- Check the rendered document against the source. The bundled validator checks structural invariants, especially headings and collapsible sections; it is not a full text-equivalence test.
- If the source uses unsupported Markdown constructs, identify them and choose an appropriate renderer or make a scoped helper improvement before claiming faithful conversion. Keep the original Markdown unchanged unless the user requested an edit.
- Keep CSS and JavaScript inline, with no external runtime dependencies in the generated document.
- The renderer makes HTTP(S), mail, telephone, relative, and fragment links clickable. Other link schemes are shown as literal text. The portal builder requires existing documents contained inside its output directory.

## Workflow

1. Inspect the source Markdown for heading depth, tables, code blocks, and less common syntax.
2. Locate this installed skill directory from the host skill listing and set `SKILL_DIR` to that absolute path. Use an available Python 3.9 or later executable as `PYTHON`; the bundled scripts use the standard library.
3. Run `scripts/render_md_html.py` for each requested theme, passing absolute or project-relative source and output paths.
4. Run `scripts/validate_html_doc.py` on each output. Inspect representative body text and links where content fidelity matters.
5. For a portal, render or copy every named HTML document into the portal output directory before running `scripts/build_docs_portal.py`. The builder writes only `index.html` and `Dockerfile`; verify every generated link resolves.
6. Before any deployment, read `references/deployment-safety.md` and follow the user's destination and approval boundaries. Preparing a bundle does not authorize publishing it.

## Example commands

```bash
"$PYTHON" "$SKILL_DIR/scripts/render_md_html.py" docs/spec.md --out docs/spec-dark.html --theme dark
"$PYTHON" "$SKILL_DIR/scripts/render_md_html.py" docs/spec.md --out docs/spec-light.html --theme light
"$PYTHON" "$SKILL_DIR/scripts/validate_html_doc.py" docs/spec.md docs/spec-dark.html
"$PYTHON" "$SKILL_DIR/scripts/validate_html_doc.py" docs/spec.md docs/spec-light.html
```

For a portal, put the linked files in the chosen output directory first:

```bash
"$PYTHON" "$SKILL_DIR/scripts/build_docs_portal.py" --out docs/portal \
  --doc "Overview|Short overview|overview-dark.html|overview-light.html" \
  --doc "Specification|Detailed reference|spec-dark.html|spec-light.html"
```

Read `references/style-contract.md` when changing CSS, layout, or interactions. Keep section rails aligned rather than adding decorative offsets.
