# Publications Metadata Workflow

This folder keeps publication metadata reproducible for the AP-style homepage.

## Why
The homepage now depends on structured fields in `_publications/*.md`:
- `topic`
- `pub_year`
- `selected`
- `author_role` (optional)

Without these fields, ordering and grouping can silently drift.

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
