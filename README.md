# Reading Challenge Tracker CLI

A local-first Python command-line tool for tracking reading goals, finished
books, ratings, and reviews. Stores everything in a local JSON file and can
export your library to CSV. No accounts, no API keys, no cloud.

Built by Dylan Asdale for **Asdale Dynamics, LLC** (Indiana, formed October
2026). Credit: Asdale Dynamics, LLC.

## Features

- Log finished books with title, author, date finished, rating (1–5), and review
- Set and track an annual reading goal
- View tally statistics: total books, average rating, books by year, rating distribution
- Export your library to CSV
- Local JSON storage under `data/books.json` (overridable with
  `READING_TRACKER_DATA`)
- Standard library only — no dependencies to install

## Usage

From the project folder:

```bash
# Log a finished book
python3 reading_tracker.py add --title "The Massive AI Manual" --author "Dylan Asdale" --rating 5 --review "Clear and friendly."

# Use a specific finish date
python3 reading_tracker.py add --title "Atomic Habits" --author "James Clear" --date 2026-01-15 --rating 4

# List logged books
python3 reading_tracker.py list

# Set an annual reading goal and check progress
python3 reading_tracker.py goal --set 12
python3 reading_tracker.py goal

# View tally statistics
python3 reading_tracker.py stats

# Export to CSV
python3 reading_tracker.py export --output books.csv
```

## Tests

Tally logic is covered by `tests/test_tally.py`:

```bash
python3 -m unittest discover -s tests -v
```

## Data

Books are stored in `data/books.json` relative to the working directory. Set
the `READING_TRACKER_DATA` environment variable to a directory path to store
the file elsewhere.

## License

MIT License. Copyright (c) 2026 Asdale Dynamics, LLC. See LICENSE.
