# Publications Metadata Workflow

This folder keeps publication metadata reproducible for the AP-style homepage.

## Why
The homepage now depends on structured fields in `_publications/*.md`:
- `topic`
- `pub_year`
- `selected`
- `author_role` (optional)

Without these fields, ordering and grouping can silently drift.

Explicit frontmatter values are authoritative. `normalize_metadata.py` fills
missing fields only; it does not overwrite curated topic, year, selected status,
or author role. Keyword/name inference is a default for an absent value, not
publication evidence. This preserves manually verified co-first/corresponding
roles and editorial selections when the heuristic's keyword or filename lists
are older than the content. In particular, HTML emphasis around an author's
name must not cause an explicit role to disappear.

Regression gate: `python3 -m unittest discover -s tools/publications -p 'test_*.py'`.
The tests cover explicit values, inferred missing values, idempotence, and every
current publication file. The 2026-09-20 fix reproduced 22 existing-file rewrites
before the change; afterwards the same files reported `changed=0` with no content
rewrites.

## Commands

From repo root:

```bash
python tools/publications/normalize_metadata.py --check
python tools/publications/normalize_metadata.py --apply
python tools/publications/audit_metadata.py
```

## Recommended update flow
1. Add/update publication markdown files.
2. Run `normalize_metadata.py --apply`.
3. Run `audit_metadata.py` and fix any issues.
4. Build preview and inspect `/`, `/research/`, `/publications/`.
5. Commit.

## Notes
- `selected` drives cards on home/research/publications.
- `pub_year` is used for sorting (descending).
- Filenames with spaces should be avoided; use `-`.
