#!/usr/bin/env python3
"""Render a Markdown file as self-contained editorial HTML."""

from __future__ import annotations

import argparse
import html
import re
from pathlib import Path
from urllib.parse import urlsplit


KEYWORDS = {
    "true", "false", "null", "yes", "no", "direct", "indirect",
    "required", "string", "number", "boolean", "array",
    "object", "source", "claim", "market", "fit", "expected", "behavior",
    "public", "private", "agent", "agents", "extract", "identify", "search",
    "classify", "explain", "save", "revisit", "input", "output", "schema",
    "version",
}

TOKEN_RE = re.compile(
    r"(\"(?:\\.|[^\"\\])*\"|'(?:\\.|[^'\\])*'|`(?:\\.|[^`\\])*`|#.*$|//.*$|"
    r"\b\d+(?:\.\d+)?\b|\b[a-zA-Z_][\w-]*\b|[{}\[\]():,./?+*\-=|>]+)",
    re.M,
)


def theme_tokens(theme: str) -> str:
    if theme == "light":
        return """      --bg: #f3efe6;
      --charcoal: #e6dece;
      --panel: rgba(255, 252, 244, 0.9);
      --panel-2: rgba(236, 230, 217, 0.95);
      --paper: #201d19;
      --text: #292620;
      --muted: #6f675c;
      --dim: #958b7d;
      --accent: #8b6f43;
      --accent-2: #5e4b2c;
      --border: rgba(32, 29, 25, 0.12);
      --border-strong: rgba(32, 29, 25, 0.2);
      --code-bg: #e8e1d4;
      --table-alt: rgba(32, 29, 25, 0.035);
      --keyword: #745725;
      --string: #58734c;
      --comment: #8a8174;
      --number: #9a5f2d;
      --punctuation: #6a6258;
      --ambient-rgb: 139, 111, 67;
      --grid-rgb: 32, 29, 25;
      --grid-alpha: 0.035;
      --intro-rgb: 41, 38, 32;"""
    return """      --bg: #0f0f0f;
      --charcoal: #151515;
      --panel: rgba(27, 27, 26, 0.9);
      --panel-2: rgba(18, 18, 17, 0.94);
      --paper: #d7cfbf;
      --text: #ece9e2;
      --muted: #a4a09a;
      --dim: #706d68;
      --accent: #b8a27d;
      --accent-2: #d3c09a;
      --border: rgba(255, 255, 255, 0.08);
      --border-strong: rgba(255, 255, 255, 0.16);
      --code-bg: #0a0a09;
      --table-alt: rgba(215, 207, 191, 0.045);
      --keyword: #d3c09a;
      --string: #9fb89f;
      --comment: #85817a;
      --number: #c99d66;
      --punctuation: #c6b89d;
      --ambient-rgb: 184, 162, 125;
      --grid-rgb: 255, 255, 255;
      --grid-alpha: 0.018;
      --intro-rgb: 236, 233, 226;"""


def css(theme: str) -> str:
    return f"""
    :root {{
{theme_tokens(theme)}
    }}
    * {{ box-sizing: border-box; }}
    html {{ scroll-behavior: smooth; }}
    body {{
      margin: 0;
      background: var(--bg);
      color: var(--text);
      font-family: "Avenir Next", "Helvetica Neue", "Segoe UI", ui-sans-serif, system-ui, sans-serif;
      font-size: 15.5px;
      line-height: 1.56;
      -webkit-font-smoothing: antialiased;
    }}
    body::before {{
      content: "";
      position: fixed;
      inset: 0;
      pointer-events: none;
      background:
        radial-gradient(circle at 23% 9%, rgba(var(--ambient-rgb), 0.09), transparent 25rem),
        repeating-linear-gradient(90deg, rgba(var(--grid-rgb), var(--grid-alpha)) 0, rgba(var(--grid-rgb), var(--grid-alpha)) 1px, transparent 1px, transparent 96px);
      opacity: 0.86;
      z-index: -1;
    }}
    a {{ color: var(--accent-2); text-decoration: none; border-bottom: 1px solid transparent; }}
    a:hover, a:focus {{ border-bottom-color: var(--accent); }}
    .toc-toggle {{ display: none; }}
    .toc {{
      position: fixed; top: 0; left: 0; bottom: 0; width: 292px;
      padding: 32px 24px; overflow-y: auto; background: var(--panel-2);
      border-right: 1px solid var(--border); backdrop-filter: blur(4px); z-index: 10;
    }}
    .toc-title {{
      margin: 0 0 16px; color: var(--muted);
      font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono", monospace;
      font-size: 0.68rem; font-weight: 500; letter-spacing: 0.08em; text-transform: uppercase;
    }}
    .toc-title::before {{
      content: ""; display: inline-block; width: 8px; height: 8px; margin-right: 9px;
      border: 1px solid rgba(var(--ambient-rgb), 0.58); border-radius: 50%;
    }}
    .toc nav ul {{ list-style: none; margin: 0; padding: 0; }}
    .toc nav li {{ margin: 0; padding: 0; }}
    .toc nav a {{
      display: block; padding: 8px 0 8px 15px; color: rgba(var(--intro-rgb), 0.88);
      border-bottom: 0; border-left: 1px solid transparent; font-size: 0.91rem;
    }}
    .toc nav a.level-2 {{ padding-left: 22px; color: var(--muted); font-size: 0.84rem; }}
    .toc nav a.level-3 {{ padding-left: 34px; color: var(--muted); font-size: 0.79rem; }}
    .toc nav a.level-4, .toc nav a.level-5, .toc nav a.level-6 {{ padding-left: 44px; color: var(--dim); font-size: 0.75rem; }}
    .toc nav a:hover, .toc nav a:focus {{ color: var(--paper); border-left-color: var(--accent); background: rgba(var(--ambient-rgb), 0.08); }}
    .controls {{ position: fixed; top: 14px; right: 14px; z-index: 20; display: flex; gap: 8px; }}
    button {{
      border: 1px solid var(--border-strong); border-radius: 5px; background: var(--panel);
      color: var(--text); font: inherit; font-size: 0.78rem; line-height: 1;
      padding: 9px 10px; cursor: pointer; backdrop-filter: blur(4px);
    }}
    button:hover, button:focus {{ border-color: rgba(var(--ambient-rgb), 0.5); color: var(--paper); background: rgba(var(--ambient-rgb), 0.08); }}
    main {{ max-width: 760px; margin: 0 auto; padding: 78px 28px 96px; }}
    h1, h2, h3, h4, h5, h6 {{ margin: 0; color: var(--paper); line-height: 1.08; }}
    h1 {{ max-width: 720px; margin: 0 0 14px; font-weight: 400; font-size: clamp(2.45rem, 7vw, 4.9rem); letter-spacing: 0; text-wrap: balance; }}
    h2 {{ font-weight: 500; font-size: 1.34rem; }}
    h3 {{ color: var(--paper); font-weight: 500; font-size: 1.04rem; }}
    h4 {{ margin: 24px 0 12px; color: var(--paper); font-size: 0.96rem; font-weight: 600; }}
    strong {{ color: var(--paper); }}
    .reading-time {{
      display: inline-block; margin: 0 0 46px; padding: 5px 0 0;
      border-top: 1px solid rgba(var(--ambient-rgb), 0.38); color: var(--muted);
      font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono", monospace;
      font-size: 0.74rem; letter-spacing: 0.02em;
    }}
    header + p {{ margin-bottom: 18px; color: var(--paper); font-size: clamp(1.24rem, 2vw, 1.52rem); line-height: 1.34; text-wrap: balance; }}
    header + p + p {{ max-width: 690px; color: rgba(var(--intro-rgb), 0.78); }}
    p {{ margin: 0 0 16px; }}
    ul, ol {{ margin: 0 0 18px 1.25rem; padding: 0; }}
    li {{ margin: 6px 0; }}
    li > p {{ margin: 6px 0; }}
    blockquote {{
      position: relative; margin: 20px 0 24px; padding: 15px 18px 15px 20px;
      border-left: 1px solid var(--accent); background: rgba(var(--ambient-rgb), 0.07); color: var(--paper);
    }}
    blockquote p {{ margin: 0; }}
    code {{ font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono", monospace; font-size: 0.92em; }}
    p code, li code, h3 code, h4 code, td code, th code {{
      padding: 1px 5px; border: 1px solid var(--border); border-radius: 3px;
      background: var(--code-bg); color: var(--paper); overflow-wrap: anywhere;
    }}
    details.section {{ position: relative; margin: 38px 0 0; padding-top: 20px; border-top: 1px solid var(--border); }}
    details.section-level-3 {{ margin-top: 25px; padding-top: 16px; border-top-style: dashed; border-top-color: var(--border); }}
    details.section::before {{
      content: ""; position: absolute; top: -4px; left: 0; width: 8px; height: 8px;
      border: 1px solid rgba(var(--ambient-rgb), 0.72); border-radius: 50%; background: var(--bg);
    }}
    details.section > summary {{ display: flex; align-items: center; gap: 12px; cursor: pointer; list-style: none; color: var(--paper); }}
    details.section > summary::-webkit-details-marker {{ display: none; }}
    details.section > summary::before {{
      content: "+"; width: 1.25rem; color: var(--accent);
      font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono", monospace; font-weight: 400; flex: 0 0 auto;
    }}
    details.section[open] > summary::before {{ content: "-"; }}
    details.section > summary h2, details.section > summary h3 {{ margin: 0; }}
    .section-body {{ padding-top: 18px; }}
    .code-block {{
      position: relative; margin: 20px 0 23px; border: 1px solid var(--border); border-radius: 5px;
      background: var(--code-bg); box-shadow: inset 0 0 0 1px rgba(var(--ambient-rgb), 0.04); overflow: hidden;
    }}
    .code-block::before {{
      content: ""; position: absolute; top: 0; left: 0; right: 0; height: 1px;
      background: linear-gradient(90deg, rgba(var(--ambient-rgb), 0.72), transparent 58%);
    }}
    .language-label {{
      position: absolute; top: 7px; left: 10px; color: var(--muted);
      font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono", monospace;
      font-size: 0.68rem; letter-spacing: 0.06em; text-transform: uppercase;
    }}
    .copy-code {{ position: absolute; top: 6px; right: 6px; padding: 6px 8px; background: var(--panel); color: var(--muted); font-size: 0.68rem; }}
    pre {{ margin: 0; padding: 38px 16px 16px; overflow-x: auto; white-space: pre; color: var(--text); font-size: 0.91rem; }}
    .tok-string {{ color: var(--string); }}
    .tok-keyword {{ color: var(--keyword); font-weight: 700; }}
    .tok-comment {{ color: var(--comment); font-style: italic; }}
    .tok-number {{ color: var(--number); }}
    .tok-punctuation {{ color: var(--punctuation); }}
    .table-wrap {{ width: 100%; overflow-x: auto; margin: 22px 0; border: 1px solid var(--border); border-radius: 5px; }}
    table {{ width: 100%; min-width: 560px; border-collapse: collapse; }}
    th, td {{ padding: 9px 11px; border-bottom: 1px solid var(--border); text-align: left; vertical-align: top; }}
    thead th {{ position: sticky; top: 0; background: var(--panel); color: var(--paper); z-index: 1; }}
    tbody tr:nth-child(even) {{ background: var(--table-alt); }}
    @media (min-width: 1140px) {{ main {{ margin-left: calc(292px + ((100vw - 292px - 760px) / 2)); margin-right: auto; }} }}
    @media (max-width: 860px) {{
      .toc-toggle {{ position: fixed; top: 12px; left: 12px; z-index: 30; display: inline-flex; }}
      .toc {{ top: 52px; left: 12px; right: 12px; bottom: auto; width: auto; max-height: calc(100vh - 70px); border: 1px solid var(--border); border-radius: 5px; display: none; }}
      body.toc-open .toc {{ display: block; }}
      .controls {{ top: 12px; right: 12px; }}
      main {{ padding: 76px 18px 58px; }}
      h1 {{ font-size: 2.35rem; }}
      pre {{ font-size: 0.86rem; }}
    }}
    @media print {{
      :root {{ --bg: #ffffff; --panel: #ffffff; --panel-2: #ffffff; --paper: #000000; --text: #000000; --muted: #333333; --accent: #000000; --accent-2: #000000; --border: #999999; --border-strong: #777777; --code-bg: #f4f4f4; }}
      body {{ background: #ffffff; color: #000000; }}
      body::before, .toc, .toc-toggle, .controls, .copy-code, .language-label {{ display: none !important; }}
      main {{ max-width: none; margin: 0; padding: 0; }}
      details.section, details.section > summary, .section-body {{ display: block !important; }}
      details.section > summary::before, details.section::before {{ content: "" !important; display: none !important; }}
      details.section:not([open]) > .section-body {{ display: block !important; }}
      a {{ color: #000000; border-bottom: 0; }}
      pre {{ white-space: pre-wrap; }}
    }}
"""


def slugify(text: str, used: set[str]) -> str:
    base = re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-") or "section"
    slug = base
    n = 2
    while slug in used:
        slug = f"{base}-{n}"
        n += 1
    used.add(slug)
    return slug


def inline(text: str) -> str:
    placeholders: list[str] = []

    def code_repl(match: re.Match[str]) -> str:
        placeholders.append(f"<code>{html.escape(match.group(1))}</code>")
        return f"@@CODE{len(placeholders)-1}@@"

    def link_repl(match: re.Match[str]) -> str:
        label = match.group(1)
        destination = html.unescape(match.group(2)).strip()
        try:
            scheme = urlsplit(html.unescape(destination)).scheme.lower()
        except ValueError:
            scheme = 'invalid'
        if scheme not in {'', 'http', 'https', 'mailto', 'tel'} or any(ord(char) < 32 for char in destination):
            return f'{label} (<code>{html.escape(destination)}</code>)'
        return f'<a href="{html.escape(destination, quote=True)}">{label}</a>'

    text = re.sub(r"`([^`]+)`", code_repl, text)
    escaped = html.escape(text, quote=False)
    escaped = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", link_repl, escaped)
    escaped = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", escaped)
    escaped = re.sub(r"\*([^*]+)\*", r"<em>\1</em>", escaped)
    for i, value in enumerate(placeholders):
        escaped = escaped.replace(f"@@CODE{i}@@", value)
    return escaped


def highlight(code: str) -> str:
    escaped = html.escape(code, quote=False)

    def repl(match: re.Match[str]) -> str:
        token = match.group(0)
        if token.startswith("#") or token.startswith("//"):
            cls = "tok-comment"
        elif token.startswith(("\"", "'", "`")):
            cls = "tok-string"
        elif re.fullmatch(r"\d+(?:\.\d+)?", token):
            cls = "tok-number"
        elif token in KEYWORDS:
            cls = "tok-keyword"
        elif re.fullmatch(r"[{}\[\]():,./?+*\-=|>]+", token):
            cls = "tok-punctuation"
        else:
            return token
        return f'<span class="{cls}">{token}</span>'

    return TOKEN_RE.sub(repl, escaped)


def render_code(code: str, lang: str) -> str:
    lang = (lang or "text").strip() or "text"
    safe_lang = html.escape(lang)
    return "\n".join([
        f'          <div class="code-block" data-language="{safe_lang}">',
        f'            <span class="language-label">{safe_lang}</span>',
        '            <button class="copy-code" type="button">Copy</button>',
        f'            <pre><code class="language-{safe_lang}">{highlight(code.rstrip())}</code></pre>',
        "          </div>",
    ])


def split_table_row(line: str) -> list[str]:
    line = line.strip()
    if line.startswith("|"):
        line = line[1:]
    if line.endswith("|"):
        line = line[:-1]
    return [cell.strip() for cell in line.split("|")]


def is_table_delim(line: str) -> bool:
    cells = split_table_row(line)
    return bool(cells) and all(re.fullmatch(r":?-{3,}:?", c.strip()) for c in cells)


def render_table(lines: list[str]) -> str:
    head = split_table_row(lines[0])
    rows = [split_table_row(x) for x in lines[2:]]
    out = ['          <div class="table-wrap">', "            <table>", "              <thead>", "                <tr>"]
    out += [f"                  <th>{inline(cell)}</th>" for cell in head]
    out += ["                </tr>", "              </thead>", "              <tbody>"]
    for row in rows:
        out.append("                <tr>")
        out += [f"                  <td>{inline(cell)}</td>" for cell in row]
        out.append("                </tr>")
    out += ["              </tbody>", "            </table>", "          </div>"]
    return "\n".join(out)


def render_list(items: list[str], ordered: bool) -> str:
    tag = "ol" if ordered else "ul"
    out = [f"          <{tag}>"]
    for item in items:
        paras = [p.strip() for p in item.split("\n") if p.strip()]
        if len(paras) <= 1:
            out.append(f"            <li>{inline(paras[0] if paras else '')}</li>")
        else:
            out.append(f"            <li>{inline(paras[0])}")
            out += [f"              <p>{inline(p)}</p>" for p in paras[1:]]
            out.append("            </li>")
    out.append(f"          </{tag}>")
    return "\n".join(out)


def markdown_body(md: str) -> tuple[str, str]:
    lines = md.splitlines()
    used: set[str] = set()
    out: list[str] = []
    para: list[str] = []
    open_sections: list[int] = []
    title = "Document"

    def flush_para() -> None:
        nonlocal para
        if para:
            text = " ".join(x.strip() for x in para).strip()
            if text:
                out.append(f"          <p>{inline(text)}</p>")
            para = []

    def close_to(level: int) -> None:
        flush_para()
        while open_sections and open_sections[-1] >= level:
            out.append("        </div>")
            out.append("      </details>")
            open_sections.pop()

    i = 0
    in_code = False
    code_lang = "text"
    code_lines: list[str] = []
    while i < len(lines):
        line = lines[i]
        fence = re.match(r"^```\s*([^`]*)$", line)
        if in_code:
            if fence:
                out.append(render_code("\n".join(code_lines), code_lang))
                in_code = False
                code_lines = []
            else:
                code_lines.append(line)
            i += 1
            continue
        if fence:
            flush_para()
            in_code = True
            code_lang = fence.group(1).strip() or "text"
            i += 1
            continue

        heading = re.match(r"^(#{1,6})\s+(.+?)\s*$", line)
        if heading:
            flush_para()
            level = len(heading.group(1))
            text = heading.group(2).strip()
            plain = re.sub(r"`([^`]+)`", r"\1", text)
            slug = slugify(plain, used)
            if level == 1 and title == "Document":
                title = plain
                words = re.findall(r"\b\w+\b", md)
                minutes = max(1, round(len(words) / 200))
                out += [
                    f'      <header id="{slug}">',
                    f"        <h1>{inline(text)}</h1>",
                    f'        <p class="reading-time">Reading time: ~{minutes} min read</p>',
                    "      </header>",
                ]
            elif level in (2, 3):
                close_to(level)
                out += [
                    f'      <details class="section section-level-{level}" id="{slug}" open>',
                    f"        <summary><h{level}>{inline(text)}</h{level}></summary>",
                    '        <div class="section-body">',
                ]
                open_sections.append(level)
            else:
                out.append(f'          <h{level} id="{slug}">{inline(text)}</h{level}>')
            i += 1
            continue

        if not line.strip():
            flush_para()
            i += 1
            continue
        if line.lstrip().startswith(">"):
            flush_para()
            q: list[str] = []
            while i < len(lines) and lines[i].lstrip().startswith(">"):
                q.append(re.sub(r"^\s*>\s?", "", lines[i]))
                i += 1
            out += ["          <blockquote>", f"            <p>{inline(' '.join(q).strip())}</p>", "          </blockquote>"]
            continue
        if line.strip().startswith("|") and i + 1 < len(lines) and is_table_delim(lines[i + 1]):
            flush_para()
            table = [line, lines[i + 1]]
            i += 2
            while i < len(lines) and lines[i].strip().startswith("|"):
                table.append(lines[i])
                i += 1
            out.append(render_table(table))
            continue
        list_match = re.match(r"^(\s*)([-*+] |\d+\. )(.*)$", line)
        if list_match:
            flush_para()
            ordered = bool(re.match(r"\d+\. ", list_match.group(2)))
            base_indent = len(list_match.group(1))
            items = []
            current = list_match.group(3)
            i += 1
            while i < len(lines):
                nxt = lines[i]
                next_match = re.match(r"^(\s*)([-*+] |\d+\. )(.*)$", nxt)
                if next_match and bool(re.match(r"\d+\. ", next_match.group(2))) == ordered and len(next_match.group(1)) == base_indent:
                    items.append(current)
                    current = next_match.group(3)
                    i += 1
                    continue
                if not nxt.strip():
                    i += 1
                    break
                if nxt.startswith(" " * (base_indent + 2)):
                    current += "\n" + nxt.strip()
                    i += 1
                    continue
                break
            items.append(current)
            out.append(render_list(items, ordered))
            continue

        para.append(line)
        i += 1

    if in_code:
        out.append(render_code("\n".join(code_lines), code_lang))
    flush_para()
    close_to(1)
    return "\n".join(out), title


SCRIPT = """
    (function () {
      var tocNav = document.getElementById("toc-nav");
      var headings = Array.prototype.slice.call(document.querySelectorAll("main h1, main h2, main h3, main h4, main h5, main h6"));
      var list = document.createElement("ul");
      headings.forEach(function (heading) {
        var target = heading.id ? heading : heading.closest("details[id]") || heading.parentElement;
        if (!target.id) target.id = heading.textContent.trim().toLowerCase().replace(/[^a-z0-9]+/g, "-").replace(/^-|-$/g, "");
        var item = document.createElement("li");
        var link = document.createElement("a");
        link.href = "#" + target.id;
        link.textContent = heading.textContent;
        link.className = "level-" + heading.tagName.slice(1);
        item.appendChild(link);
        list.appendChild(item);
      });
      tocNav.appendChild(list);
      document.querySelector(".toc-toggle").addEventListener("click", function () {
        var open = !document.body.classList.contains("toc-open");
        document.body.classList.toggle("toc-open", open);
        this.setAttribute("aria-expanded", String(open));
      });
      tocNav.addEventListener("click", function (event) {
        if (event.target.tagName === "A") {
          document.body.classList.remove("toc-open");
          document.querySelector(".toc-toggle").setAttribute("aria-expanded", "false");
        }
      });
      document.getElementById("collapse-all").addEventListener("click", function () {
        document.querySelectorAll("details.section").forEach(function (section) { section.removeAttribute("open"); });
      });
      document.getElementById("expand-all").addEventListener("click", function () {
        document.querySelectorAll("details.section").forEach(function (section) { section.setAttribute("open", ""); });
      });
      document.querySelectorAll(".copy-code").forEach(function (button) {
        button.addEventListener("click", function () {
          var code = button.parentElement.querySelector("code").innerText;
          function markCopied() {
            var original = button.textContent;
            button.textContent = "Copied";
            window.setTimeout(function () { button.textContent = original; }, 1200);
          }
          if (navigator.clipboard && navigator.clipboard.writeText) {
            navigator.clipboard.writeText(code).then(markCopied);
            return;
          }
          var textarea = document.createElement("textarea");
          textarea.value = code;
          textarea.setAttribute("readonly", "");
          textarea.style.position = "fixed";
          textarea.style.left = "-9999px";
          document.body.appendChild(textarea);
          textarea.select();
          document.execCommand("copy");
          document.body.removeChild(textarea);
          markCopied();
        });
      });
      var printState = [];
      window.addEventListener("beforeprint", function () {
        printState = [];
        document.querySelectorAll("details.section").forEach(function (section) {
          printState.push([section, section.hasAttribute("open")]);
          section.setAttribute("open", "");
        });
      });
      window.addEventListener("afterprint", function () {
        printState.forEach(function (entry) { if (!entry[1]) entry[0].removeAttribute("open"); });
      });
    })();
"""


def render(md_path: Path, out_path: Path, theme: str) -> None:
    md = md_path.read_text()
    body, title = markdown_body(md)
    html_doc = f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{html.escape(title)}</title>
  <style>
{css(theme)}
  </style>
</head>
<body>
  <button class="toc-toggle" type="button" aria-controls="toc" aria-expanded="false">Contents</button>
  <aside class="toc" id="toc" aria-label="Table of contents">
    <p class="toc-title">Contents</p>
    <nav id="toc-nav"></nav>
  </aside>
  <div class="controls" aria-label="Section controls">
    <button type="button" id="collapse-all">Collapse All</button>
    <button type="button" id="expand-all">Expand All</button>
  </div>
  <main>
    <article>
{body}
    </article>
  </main>
  <script>
{SCRIPT}
  </script>
</body>
</html>
"""
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(html_doc)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("markdown", type=Path)
    parser.add_argument("--out", type=Path, required=True)
    parser.add_argument("--theme", choices=["dark", "light"], default="dark")
    args = parser.parse_args()
    render(args.markdown, args.out, args.theme)
    print(f"wrote {args.out}")


if __name__ == "__main__":
    main()
