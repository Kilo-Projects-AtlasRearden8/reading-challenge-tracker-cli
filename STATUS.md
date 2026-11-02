# STATUS

## What was built

A local-first Python CLI for tracking reading goals, finished books, ratings,
and reviews, built for Dylan Asdale / Asdale Dynamics, LLC.

Files:
- `reading_tracker.py` — CLI (stdlib only): `add`, `list`, `goal`, `stats`,
  `export` subcommands
- `tally.py` — pure tally logic: count, books by year, average rating, rating
  distribution, goal progress
- `storage.py` — local JSON storage (`data/books.json`, overridable via
  `READING_TRACKER_DATA`) and CSV export
- `tests/test_tally.py` — unit tests for tally logic (unittest)
- `tests/test_storage.py` — unit tests for storage roundtrip, edge cases, and
  CSV export (unittest)
- `README.md` — beginner-friendly usage guide (credits Asdale Dynamics, LLC)
- `LICENSE` — MIT, Copyright (c) 2026 Asdale Dynamics, LLC
- `STATUS.md` — this file
- `.gitignore` — ignores `__pycache__/`, `*.pyc`, `data/`, build artifacts

## How to run

You only need Python 3.7+. Nothing else to install.

```bash
# Log a finished book
python3 reading_tracker.py add --title "Title" --author "Author" \
  --rating 5 --review "Review text"

# With a specific finish date
python3 reading_tracker.py add --title "Title" --author "Author" \
  --date 2026-01-15 --rating 4

# List books
python3 reading_tracker.py list

# Set annual goal and check progress
python3 reading_tracker.py goal --set 12
python3 reading_tracker.py goal

# Tally statistics
python3 reading_tracker.py stats

# Export to CSV
python3 reading_tracker.py export --output books.csv

# Run tests
python3 -m unittest discover -s tests -v
```

Data lives in `data/books.json` next to the working directory. Set
`READING_TRACKER_DATA` to a directory path to store it elsewhere. No accounts,
no API keys, no network.

## Verification results

- `python3 -m unittest discover -s tests -v`: 14 tests, OK (8 tally + 6 storage)
- CLI smoke test (add x2, goal, stats, list, export): all subcommands run
  successfully; CSV output has correct header and rows
- LICENSE copyright line: `Copyright (c) 2026 Asdale Dynamics, LLC` (exact)
- README credits Asdale Dynamics, LLC
- Python 3.13.5, standard library only, no dependencies installed
- No `.github/workflows` directory present
- No secrets, API keys, or personal data in files

## Known gaps

- No input deduplication (adding the same book twice creates two entries)
- No edit/delete commands for logged books
- Goal is a single integer, not per-year
- `data/` directory is created at runtime; not committed
