"""Tally logic for the reading challenge tracker.

Pure functions over a list of book dicts. Each book dict has keys:
title, author, date_finished (ISO YYYY-MM-DD), rating (1-5 or None),
review (str).
"""

from __future__ import annotations

from collections import Counter
from datetime import date
from typing import Iterable


def count_books(books: Iterable[dict]) -> int:
    """Return the total number of books."""
    return sum(1 for _ in books)


def books_by_year(books: Iterable[dict]) -> dict[int, int]:
    """Return a mapping of year -> number of books finished that year."""
    counts: Counter[int] = Counter()
    for book in books:
        finished = book.get("date_finished")
        if not finished:
            continue
        try:
            year = date.fromisoformat(finished).year
        except ValueError:
            continue
        counts[year] += 1
    return dict(counts)


def average_rating(books: Iterable[dict]) -> float | None:
    """Return the average rating of rated books, or None if none are rated."""
    ratings = [int(book["rating"]) for book in books if book.get("rating") is not None]
    if not ratings:
        return None
    return sum(ratings) / len(ratings)


def ratings_distribution(books: Iterable[dict]) -> dict[int, int]:
    """Return a mapping of rating value -> number of books with that rating."""
    dist: Counter[int] = Counter()
    for book in books:
        rating = book.get("rating")
        if rating is not None:
            dist[int(rating)] += 1
    return dict(dist)


def goal_progress(books: Iterable[dict], goal: int) -> dict:
    """Return progress toward a reading goal.

    Keys: goal, finished, remaining, percent, met.
    """
    books = list(books)
    finished = count_books(books)
    remaining = max(goal - finished, 0)
    percent = (finished / goal * 100) if goal > 0 else 0.0
    return {
        "goal": goal,
        "finished": finished,
        "remaining": remaining,
        "percent": round(percent, 1),
        "met": finished >= goal,
    }
