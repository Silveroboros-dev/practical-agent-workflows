#!/usr/bin/env python3
"""Validate an editorial HTML document against its Markdown source."""

from __future__ import annotations

import argparse
import re
from html.parser import HTMLParser
from pathlib import Path


class DocParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.headings: list[tuple[int, str]] = []
        self.details = 0
        self.open_details = 0
        self.external_scripts = 0
        self.link_tags = 0
        self.tables = 0
        self._heading_tag: str | None = None
        self._heading_buf: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attrs_dict = dict(attrs)
        if tag in {"h1", "h2", "h3", "h4", "h5", "h6"}:
            self._heading_tag = tag
            self._heading_buf = []
        if tag == "details":
            self.details += 1
            if "open" in attrs_dict:
                self.open_details += 1
        if tag == "script" and "src" in attrs_dict:
            self.external_scripts += 1
        if tag == "link":
            self.link_tags += 1
        if tag == "table":
            self.tables += 1

    def handle_data(self, data: str) -> None:
        if self._heading_tag:
            self._heading_buf.append(data)

    def handle_endtag(self, tag: str) -> None:
        if self._heading_tag and tag == self._heading_tag:
            self.headings.append((int(tag[1]), "".join(self._heading_buf).strip()))
            self._heading_tag = None
            self._heading_buf = []


def md_headings(md: str) -> list[tuple[int, str]]:
    headings = []
    in_fence = False
    for line in md.splitlines():
        if line.startswith('```'):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        match = re.match(r"^(#{1,6})\s+(.+)$", line)
        if match:
            headings.append((len(match.group(1)), re.sub(r"`([^`]+)`", r"\1", match.group(2).strip())))
    return headings


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("markdown", type=Path)
    parser.add_argument("html", type=Path)
    args = parser.parse_args()

    expected = md_headings(args.markdown.read_text())
    html_text = args.html.read_text()
    parsed = DocParser()
    parsed.feed(html_text)

    failures: list[str] = []
    if parsed.headings != expected:
        failures.append(f"heading mismatch: md={len(expected)} html={len(parsed.headings)}")
    expected_details = sum(1 for level, _ in expected if level in (2, 3))
    if parsed.details != expected_details:
        failures.append(f"details count mismatch: expected={expected_details} actual={parsed.details}")
    if parsed.open_details != parsed.details:
        failures.append("not all details sections are open by default")
    if parsed.external_scripts or parsed.link_tags:
        failures.append("external script or link tag found")
    forbidden = [
        r"<script[^>]+src=",
        r"<link\b",
        r"@import",
        r"nth-of-type\(even\)",
        r"nth-of-type\(3n\)",
        r"margin-left:\s*clamp",
        r"padding-left:\s*clamp",
    ]
    for pattern in forbidden:
        if re.search(pattern, html_text):
            failures.append(f"forbidden pattern found: {pattern}")

    if failures:
        for failure in failures:
            print(f"FAIL: {failure}")
        raise SystemExit(1)

    print({
        "same_headings": True,
        "headings": len(expected),
        "details": parsed.details,
        "open_details": parsed.open_details,
        "tables": parsed.tables,
        "external_scripts": parsed.external_scripts,
        "link_tags": parsed.link_tags,
    })


if __name__ == "__main__":
    main()
