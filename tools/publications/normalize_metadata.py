#!/usr/bin/env python3
"""Normalize publication metadata for homepage rendering.

Usage:
  python tools/publications/normalize_metadata.py --apply
  python tools/publications/normalize_metadata.py --check
"""

from __future__ import annotations

import argparse
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PUB_DIR = ROOT / "_publications"

TRACK_BIOMED = "Translational Biomedical AI"
TRACK_GEN = "Controllable Multimodal Generation"
TRACK_PERCEPTION = "Multimodal Perception and Understanding"

SELECTED_FILES = {
    "1044.md", "1043.md", "1042-1.md", "1045.md",
    "1038.md", "1040-0.md", "1040-1.md", "1042-0.md", "1042-2.md", "0033.md", "0034.md",
    "1128.md", "1034.md", "1011.md", "1006.md", "1003.md", "1033.md", "1039.md",
}

MANUAL_YEAR = {
    "1044.md": 2026,
    "1043.md": 2025,
    "1045.md": 2025,
    "0038.md": 2025,
    "0031.md": 2024,
    "0030.md": 2024,
    "0019.md": 2023,
}


def parse_frontmatter(text: str) -> tuple[str, list[str], str]:
    m = re.match(r"^(---\n)(.*?)(\n---\n.*)$", text, re.S)
    if not m:
        raise ValueError("Missing YAML frontmatter")
    start, middle, rest = m.groups()
    return start, middle.splitlines(), rest


def infer_topic(title: str, venue: str, fn: str) -> str:
    t = f"{title} {venue}".lower()
    biomed_kw = ["clinical", "medical", "medsam", "x-ray", "ehr", "disease", "pulmonary", "digital medicine", "clines", "biomedical"]
    gen_kw = ["diffusion", "text-to-image", "image editing", "insert anything", "in-context edit", "dreamrenderer", "3dis", "migc", "generative", "gaussian", "avatar", "matting", "nerf", "face generation", "image synthesis"]

    if any(k in t for k in biomed_kw):
        return TRACK_BIOMED
    if any(k in t for k in gen_kw):
        return TRACK_GEN

    if fn in {"1128.md", "1034.md"}:
        return TRACK_PERCEPTION
    return TRACK_PERCEPTION


def infer_year(venue: str, date_value: str, fn: str) -> int:
    if fn in MANUAL_YEAR:
        return MANUAL_YEAR[fn]
    for src in (venue or "", date_value or "", fn):
        m = re.search(r"(19|20)\d{2}", src)
        if m:
            y = int(m.group())
            if 2000 <= y <= 2035:
                return y
    return 2025


def infer_author_role(author: str) -> str | None:
    role = None
    if re.search(r"Zongxin Yang\*", author):
        role = "Co-first Author"
    if re.search(r"Zongxin Yang[^,]*✉", author):
        role = "Corresponding Author" if role is None else f"{role} / Corresponding Author"

    first = author.split(",")[0].strip() if author else ""
    if "Zongxin Yang" in first and role is None:
        role = "First Author"
    return role


def normalize_lines(fn: str, lines: list[str]) -> list[str]:
    kv = {}
    for line in lines:
        s = line.strip()
        if ":" in s and not s.startswith("#"):
            k, v = s.split(":", 1)
            kv[k.strip()] = v.strip().strip('"\'')

    title = kv.get("title", "")
    venue = kv.get("venue", "")
    date_value = kv.get("date", "")
    author = kv.get("author", "")

    topic = infer_topic(title, venue, fn)
    year = infer_year(venue, date_value, fn)
    selected = "true" if fn in SELECTED_FILES else "false"
    author_role = infer_author_role(author)

    cleaned = []
    for line in lines:
        key = line.strip().split(":", 1)[0].strip() if ":" in line else ""
        if key in {"topic", "pub_year", "selected", "author_role"}:
            continue
        cleaned.append(line)

    out = []
    inserted_author_role = False
    for line in cleaned:
        out.append(line)
        if line.strip().startswith("author:") and author_role:
            out.append(f'author_role: "{author_role}"')
            inserted_author_role = True

    if author_role and not inserted_author_role:
        out.append(f'author_role: "{author_role}"')

    out.append(f'topic: "{topic}"')
    out.append(f"pub_year: {year}")
    out.append(f"selected: {selected}")
    return out


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--apply", action="store_true", help="Write normalized metadata to files")
    parser.add_argument("--check", action="store_true", help="Only report drift")
    args = parser.parse_args()

    if not args.apply and not args.check:
        parser.error("Use --apply or --check")

    changed = 0
    files = sorted(PUB_DIR.glob("*.md"))
    for fp in files:
        text = fp.read_text(encoding="utf-8")
        start, lines, rest = parse_frontmatter(text)
        normalized = normalize_lines(fp.name, lines)
        new_text = start + "\n".join(normalized) + rest
        if new_text != text:
            changed += 1
            if args.apply:
                fp.write_text(new_text, encoding="utf-8")

    mode = "APPLY" if args.apply else "CHECK"
    print(f"[{mode}] files={len(files)} changed={changed}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
