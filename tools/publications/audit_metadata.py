#!/usr/bin/env python3
"""Audit publication metadata quality for homepage rendering."""

from __future__ import annotations

import re
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PUB_DIR = ROOT / "_publications"
REQ = ["title", "author", "topic", "pub_year", "selected", "venue"]


def parse_kv(text: str) -> dict[str, str]:
    m = re.match(r"^---\n(.*?)\n---", text, re.S)
    if not m:
        return {}
    d: dict[str, str] = {}
    for line in m.group(1).splitlines():
        s = line.strip()
        if not s or s.startswith("#") or ":" not in s:
            continue
        k, v = s.split(":", 1)
        d[k.strip()] = v.strip().strip('"\'')
    return d


def main() -> int:
    files = sorted(PUB_DIR.glob("*.md"))
    issues = []
    topics = Counter()
    years = Counter()

    for fp in files:
        d = parse_kv(fp.read_text(encoding="utf-8"))
        if not d:
            issues.append((fp.name, "missing frontmatter"))
            continue

        for k in REQ:
            if not d.get(k):
                issues.append((fp.name, f"missing {k}"))

        if " " in fp.name:
            issues.append((fp.name, "filename contains spaces"))

        topics[d.get("topic", "UNKNOWN")] += 1
        years[d.get("pub_year", "UNKNOWN")] += 1

    print(f"Total files: {len(files)}")
    print("Topic distribution:")
    for k, v in topics.most_common():
        print(f"  - {k}: {v}")

    print("Year distribution (top 10):")
    for k, v in years.most_common(10):
        print(f"  - {k}: {v}")

    if issues:
        print(f"\nIssues ({len(issues)}):")
        for fn, msg in issues[:100]:
            print(f"  - {fn}: {msg}")
        return 1

    print("\nAudit passed ✅")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
