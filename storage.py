"""Local JSON storage and CSV export for the reading tracker."""

from __future__ import annotations

import csv
import json
import os
from typing import Any

DEFAULT_FILENAME = "books.json"


def data_path(filename: str = DEFAULT_FILENAME) -> str:
    """Resolve the storage file path.

    Honor READING_TRACKER_DATA as a directory override; otherwise store
    data/<filename> in the current working directory. Local-first.
    """
    env_dir = os.environ.get("READING_TRACKER_DATA")
    directory = env_dir if env_dir else "data"
    return os.path.join(directory, filename)


def load_books(path: str) -> list[dict]:
    """Load books from a JSON file. Missing or invalid files return []."""
    if not os.path.exists(path):
        return []
    try:
        with open(path, "r", encoding="utf-8") as fh:
            data = json.load(fh)
    except (json.JSONDecodeError, OSError):
        return []
    if not isinstance(data, list):
        return []
    return data


def save_books(path: str, books: list[dict]) -> None:
    """Atomically-ish write books to a JSON file, creating directories."""
    directory = os.path.dirname(path)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(path, "w", encoding="utf-8") as fh:
        json.dump(books, fh, indent=2, ensure_ascii=False)
        fh.write("\n")


def export_csv(books: list[dict], path: str) -> None:
    """Export books to a CSV file."""
    directory = os.path.dirname(path)
    if directory:
        os.makedirs(directory, exist_ok=True)
    fields = ["title", "author", "date_finished", "rating", "review"]
    with open(path, "w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=fields, extrasaction="ignore")
        writer.writeheader()
        for book in books:
            writer.writerow({field: book.get(field, "") for field in fields})
