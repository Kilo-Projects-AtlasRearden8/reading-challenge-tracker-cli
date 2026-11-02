# Reading Challenge Tracker CLI

A friendly, local-first command-line tool for tracking your reading goals,
finished books, ratings, and reviews. Everything stays on your computer in a
simple JSON file, and you can export your library to CSV whenever you like. No
accounts, no API keys, no cloud, no internet required.

Built by Dylan Asdale for **Asdale Dynamics, LLC** (Indiana, formed October
2026). Credit: Asdale Dynamics, LLC.

This tool is part of Asdale Dynamics' focus on practical, beginner-friendly
tools — plain English, step by step, never condescending.

## What it does

- Log a book you've finished: title, author, date finished, rating (1–5), and
  an optional review
- Set a yearly reading goal and watch your progress
- See your stats: total books finished, average rating, books by year, and
  how your ratings break down
- Export your whole library to a CSV file (opens in Excel, Google Sheets,
  Numbers, or any text editor)

## Get started

You only need Python (3.7 or later). Nothing else to install.

From the folder where you saved this project, run:

```bash
python3 reading_tracker.py add --title "The Massive AI Manual" \
  --author "Dylan Asdale" --rating 5 \
  --review "Clear, friendly, and step by step."
```

That logs your first book. Try a few more:

```bash
python3 reading_tracker.py add --title "Atomic Habits" \
  --author "James Clear" --date 2026-01-15 --rating 4

python3 reading_tracker.py add --title "Deep Work" \
  --author "Cal Newport" --rating 5 --review "Helped me focus."
```

### See your books

```bash
python3 reading_tracker.py list
```

You'll get a numbered list with each book's title, author, finish date, and
rating. Any review you wrote shows underneath.

### Set a reading goal

```bash
python3 reading_tracker.py goal --set 12
```

Then check your progress anytime:

```bash
python3 reading_tracker.py goal
```

It tells you how many books you've finished out of your goal, the percentage,
and whether you've met it.

### See your stats

```bash
python3 reading_tracker.py stats
```

Shows your total books finished, average rating, books grouped by year, and a
count of how many books got each star rating.

### Export your library

```bash
python3 reading_tracker.py export --output my-books.csv
```

This writes every book to `my-books.csv`, which you can open in a spreadsheet
or share however you like.

## Commands at a glance

| Command | What it does |
|---------|--------------|
| `add` | Log a finished book (`--title`, `--author`, `--date`, `--rating`, `--review`) |
| `list` | Show every book you've logged |
| `goal` | Set or check your yearly reading goal (`--set N`) |
| `stats` | Show totals, average rating, books by year, rating breakdown |
| `export` | Write all books to a CSV file (`--output path`) |

Run `python3 reading_tracker.py --help` for the full command list.

## Where your data lives

Your books are saved to `data/books.json` in the folder where you run the
tool. If you'd rather store them somewhere else, set the
`READING_TRACKER_DATA` environment variable to a folder path before running
the tool. Nothing ever leaves your machine unless you choose to export it.

## Tests

The tally logic (counts, averages, goal progress, and more) is tested with
Python's built-in `unittest`:

```bash
python3 -m unittest discover -s tests -v
```

You should see all tests pass.

## License

MIT License. Copyright (c) 2026 Asdale Dynamics, LLC. See the `LICENSE` file.

## About Asdale Dynamics, LLC

Asdale Dynamics, LLC is an Indiana company founded by Dylan Asdale — a
registered nurse turned AI author. The LLC publishes beginner-friendly AI
education, books, guides, and practical tools, including this reading tracker.
Learn more at dylanasdale.github.io.
