#!/usr/bin/env python3
"""Reading Challenge Tracker CLI.

Track reading goals, finished books, ratings, and reviews with local JSON
storage and CSV export. Local-first: no accounts, no API keys, no cloud.
"""

from __future__ import annotations

import argparse
import sys
from datetime import date

from storage import data_path, export_csv, load_books, save_books
from tally import average_rating, books_by_year, count_books, goal_progress, ratings_distribution


def validate_date(value: str) -> str:
    date.fromisoformat(value)  # raises ValueError on bad input
    return value


def validate_rating(value: str) -> int:
    rating = int(value)
    if rating < 1 or rating > 5:
        raise argparse.ArgumentTypeError("rating must be between 1 and 5")
    return rating


def cmd_add(args: argparse.Namespace) -> int:
    path = data_path()
    books = load_books(path)
    book = {
        "title": args.title,
        "author": args.author,
        "date_finished": args.date or date.today().isoformat(),
        "rating": args.rating,
        "review": args.review or "",
    }
    books.append(book)
    save_books(path, books)
    print(f"Added '{args.title}' by {args.author}.")
    return 0


def cmd_list(args: argparse.Namespace) -> int:
    books = load_books(data_path())
    if not books:
        print("No books logged yet.")
        return 0
    for i, book in enumerate(books, 1):
        rating = book.get("rating")
        rating_str = f"{rating}/5" if rating is not None else "unrated"
        print(f"{i}. {book.get('title')} — {book.get('author')} ({book.get('date_finished')}) [{rating_str}]")
        if book.get("review"):
            print(f"    {book['review']}")
    return 0


def cmd_goal(args: argparse.Namespace) -> int:
    books = load_books(data_path())
    if args.set is not None:
        progress = goal_progress(books, args.set)
        print(f"Reading goal set to {args.set} books.")
        print(f"Progress: {progress['finished']}/{progress['goal']} ({progress['percent']}%)")
    else:
        print(f"Books finished: {count_books(books)}. No goal set.")
    return 0


def cmd_stats(args: argparse.Namespace) -> int:
    books = load_books(data_path())
    if not books:
        print("No books logged yet.")
        return 0
    print(f"Total books finished: {count_books(books)}")
    avg = average_rating(books)
    if avg is not None:
        print(f"Average rating: {avg:.2f}/5")
    by_year = books_by_year(books)
    print("Books by year:")
    for year in sorted(by_year):
        print(f"  {year}: {by_year[year]}")
    dist = ratings_distribution(books)
    print("Rating distribution:")
    for rating in sorted(dist):
        label = "star" if rating == 1 else "stars"
        print(f"  {rating} {label}: {dist[rating]}")
    return 0


def cmd_export(args: argparse.Namespace) -> int:
    books = load_books(data_path())
    export_csv(books, args.output)
    print(f"Exported {len(books)} books to {args.output}.")
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Reading Challenge Tracker CLI — track reading goals, books, ratings, and reviews locally."
    )
    sub = parser.add_subparsers(dest="command", required=True)

    p_add = sub.add_parser("add", help="Log a finished book")
    p_add.add_argument("--title", required=True, help="Book title")
    p_add.add_argument("--author", required=True, help="Book author")
    p_add.add_argument("--date", type=validate_date, help="Date finished (YYYY-MM-DD), defaults to today")
    p_add.add_argument("--rating", type=validate_rating, help="Rating 1-5")
    p_add.add_argument("--review", help="Review text")
    p_add.set_defaults(func=cmd_add)

    p_list = sub.add_parser("list", help="List logged books")
    p_list.set_defaults(func=cmd_list)

    p_goal = sub.add_parser("goal", help="Show or set the annual reading goal")
    p_goal.add_argument("--set", type=int, metavar="N", help="Set the goal to N books")
    p_goal.set_defaults(func=cmd_goal)

    p_stats = sub.add_parser("stats", help="Show tally statistics")
    p_stats.set_defaults(func=cmd_stats)

    p_export = sub.add_parser("export", help="Export books to CSV")
    p_export.add_argument("--output", required=True, help="CSV output path")
    p_export.set_defaults(func=cmd_export)

    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
