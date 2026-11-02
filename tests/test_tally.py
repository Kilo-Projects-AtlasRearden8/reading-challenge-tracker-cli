"""Tests for the reading tracker tally logic."""

import unittest

from tally import average_rating, books_by_year, count_books, goal_progress, ratings_distribution

BOOKS = [
    {"title": "Book A", "author": "Author X", "date_finished": "2026-01-10", "rating": 5, "review": "Loved it."},
    {"title": "Book B", "author": "Author Y", "date_finished": "2026-02-20", "rating": 4, "review": "Good read."},
    {"title": "Book C", "author": "Author Z", "date_finished": "2025-12-01", "rating": 3, "review": "Fine."},
    {"title": "Book D", "author": "Author W", "date_finished": "2026-03-05", "rating": None, "review": ""},
]


class TestTally(unittest.TestCase):
    def test_count_books(self):
        self.assertEqual(count_books(BOOKS), 4)
        self.assertEqual(count_books([]), 0)

    def test_books_by_year(self):
        self.assertEqual(books_by_year(BOOKS), {2026: 3, 2025: 1})
        self.assertEqual(books_by_year([]), {})

    def test_books_by_year_skips_bad_dates(self):
        books = [{"title": "X", "author": "Y", "date_finished": "not-a-date", "rating": 1}]
        self.assertEqual(books_by_year(books), {})

    def test_average_rating(self):
        self.assertAlmostEqual(average_rating(BOOKS), 4.0)
        self.assertIsNone(average_rating([]))
        self.assertIsNone(average_rating([{"title": "X", "author": "Y", "rating": None}]))

    def test_ratings_distribution(self):
        self.assertEqual(ratings_distribution(BOOKS), {5: 1, 4: 1, 3: 1})
        self.assertEqual(ratings_distribution([]), {})

    def test_goal_progress_not_met(self):
        progress = goal_progress(BOOKS, 10)
        self.assertEqual(progress["goal"], 10)
        self.assertEqual(progress["finished"], 4)
        self.assertEqual(progress["remaining"], 6)
        self.assertEqual(progress["percent"], 40.0)
        self.assertFalse(progress["met"])

    def test_goal_progress_met(self):
        progress = goal_progress(BOOKS, 3)
        self.assertTrue(progress["met"])
        self.assertEqual(progress["remaining"], 0)
        self.assertEqual(progress["percent"], 133.3)

    def test_goal_progress_zero_goal(self):
        progress = goal_progress(BOOKS, 0)
        self.assertEqual(progress["percent"], 0.0)
        self.assertTrue(progress["met"])


if __name__ == "__main__":
    unittest.main()
