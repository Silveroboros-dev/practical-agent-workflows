#!/usr/bin/env python3
"""Build a static index page for a set of dark/light HTML documents."""

from __future__ import annotations

import argparse
import html
from pathlib import Path
from urllib.parse import unquote, urlsplit


def parse_doc(raw: str) -> tuple[str, str, str, str]:
    parts = raw.split("|")
    if len(parts) != 4:
        raise SystemExit("--doc must be 'Title|Description|dark-file.html|light-file.html'")
    return tuple(parts)  # type: ignore[return-value]


def validate_document(root: Path, destination: str) -> None:
    parsed = urlsplit(destination)
    relative = Path(unquote(parsed.path))
    target = (root / relative).resolve()
    if parsed.scheme or parsed.netloc or relative.is_absolute() or root.resolve() not in target.parents:
        raise SystemExit('Portal links must refer to documents inside --out: ' + destination)
    if not target.is_file():
        raise SystemExit('Render or copy the linked document into --out first: ' + destination)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", type=Path, required=True)
    parser.add_argument("--title", default="HTML Documents")
    parser.add_argument("--subtitle", default="Self-contained HTML reading documents in dark and light modes.")
    parser.add_argument("--service-name", default="docs")
    parser.add_argument("--doc", action="append", required=True)
    args = parser.parse_args()

    args.out.mkdir(parents=True, exist_ok=True)
    docs = [parse_doc(item) for item in args.doc]
    for _, _, dark, light in docs:
        validate_document(args.out, dark)
        validate_document(args.out, light)
    cards = []
    for title, desc, dark, light in docs:
        cards.append(f"""
      <article>
        <div>
          <h2>{html.escape(title)}</h2>
          <p>{html.escape(desc)}</p>
        </div>
        <div class="actions"><a href="{html.escape(dark)}">Dark</a><a href="{html.escape(light)}">Light</a></div>
      </article>""")

    index = f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{html.escape(args.title)}</title>
  <style>
    :root {{ --bg:#0f0f0f; --panel:rgba(27,27,26,.92); --paper:#d7cfbf; --text:#ece9e2; --muted:#a4a09a; --accent:#b8a27d; --line:rgba(255,255,255,.1); }}
    * {{ box-sizing:border-box; }}
    body {{ margin:0; min-height:100vh; color:var(--text); background:radial-gradient(circle at 24% 12%, rgba(184,162,125,.08), transparent 28rem), repeating-linear-gradient(90deg, rgba(255,255,255,.018) 0, rgba(255,255,255,.018) 1px, transparent 1px, transparent 96px), var(--bg); font-family:"Avenir Next","Helvetica Neue","Segoe UI",ui-sans-serif,system-ui,sans-serif; line-height:1.55; }}
    main {{ width:min(980px, calc(100% - 40px)); margin:0 auto; padding:64px 0 82px; }}
    header {{ max-width:760px; margin-bottom:52px; }}
    .kicker {{ margin:0 0 13px; color:var(--accent); font-family:ui-monospace,SFMono-Regular,Menlo,Monaco,Consolas,monospace; font-size:11px; text-transform:uppercase; letter-spacing:.08em; }}
    h1 {{ margin:0; color:var(--paper); font-size:clamp(42px,7vw,76px); font-weight:400; line-height:.98; letter-spacing:0; text-wrap:balance; }}
    .sub {{ max-width:700px; margin:22px 0 0; color:var(--muted); font-size:16px; }}
    .grid {{ display:grid; grid-template-columns:repeat(3,minmax(0,1fr)); gap:14px; }}
    article {{ border:1px solid var(--line); background:var(--panel); border-radius:5px; padding:18px; min-height:210px; display:flex; flex-direction:column; justify-content:space-between; }}
    article::before {{ content:""; width:9px; height:9px; border:1px solid rgba(184,162,125,.7); border-radius:50%; margin-bottom:22px; }}
    h2 {{ margin:0 0 12px; color:var(--paper); font-size:22px; font-weight:500; line-height:1.12; }}
    p {{ margin:0; color:var(--muted); font-size:14px; }}
    .actions {{ display:flex; flex-wrap:wrap; gap:8px; margin-top:22px; }}
    a {{ color:var(--text); text-decoration:none; border:1px solid var(--line); border-radius:5px; padding:8px 10px; font-size:13px; }}
    a:hover,a:focus {{ color:var(--paper); border-color:rgba(184,162,125,.5); background:rgba(184,162,125,.08); }}
    footer {{ margin-top:34px; color:var(--muted); font-size:13px; }}
    @media (max-width:820px) {{ .grid {{ grid-template-columns:1fr; }} main {{ padding-top:42px; }} }}
  </style>
</head>
<body>
  <main>
    <header>
      <p class="kicker">{html.escape(args.service_name)}</p>
      <h1>{html.escape(args.title)}</h1>
      <p class="sub">{html.escape(args.subtitle)}</p>
    </header>
    <section class="grid" aria-label="Documents">
{''.join(cards)}
    </section>
    <footer>Static docs bundle</footer>
  </main>
</body>
</html>
"""
    (args.out / "index.html").write_text(index)
    dockerfile = 'FROM python:3.12-slim\nWORKDIR /app\nCOPY . /app\nENV PORT=8080\nCMD ["sh", "-c", "python -m http.server ${PORT} --bind 0.0.0.0"]\n'
    (args.out / "Dockerfile").write_text(dockerfile)
    print(f"wrote {args.out / 'index.html'}")


if __name__ == "__main__":
    main()
