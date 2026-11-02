"""Tests for local JSON storage and CSV export."""

import csv
import json
import os
import tempfile
import unittest

from storage import data_path, export_csv, load_books, save_books


class TestStorage(unittest.TestCase):
    def test_save_and_load_roundtrip(self):
        books = [
            {
                "title": "Test Book",
                "author": "Test Author",
                "date_finished": "2026-01-01",
                "rating": 5,
                "review": "Great.",
            }
        ]
        with tempfile.TemporaryDirectory() as tmp:
            path = os.path.join(tmp, "books.json")
            save_books(path, books)
            loaded = load_books(path)
            self.assertEqual(loaded, books)

    def test_load_missing_file_returns_empty(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = os.path.join(tmp, "does-not-exist.json")
            self.assertEqual(load_books(path), [])

    def test_load_invalid_json_returns_empty(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = os.path.join(tmp, "bad.json")
            with open(path, "w", encoding="utf-8") as fh:
                fh.write("{not valid json")
            self.assertEqual(load_books(path), [])

    def test_load_non_list_returns_empty(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = os.path.join(tmp, "notlist.json")
            with open(path, "w", encoding="utf-8") as fh:
                json.dump({"not": "a list"}, fh)
            self.assertEqual(load_books(path), [])

    def test_export_csv_writes_header_and_rows(self):
        books = [
            {
                "title": "Book One",
                "author": "Author A",
                "date_finished": "2026-01-01",
                "rating": 5,
                "review": "Loved it.",
            },
            {
                "title": "Book Two",
                "author": "Author B",
                "date_finished": "2026-02-01",
                "rating": 4,
                "review": "",
            },
        ]
        with tempfile.TemporaryDirectory() as tmp:
            path = os.path.join(tmp, "out.csv")
            export_csv(books, path)
            with open(path, newline="", encoding="utf-8") as fh:
                reader = list(csv.reader(fh))
            self.assertEqual(
                reader[0], ["title", "author", "date_finished", "rating", "review"]
            )
            self.assertEqual(reader[1][0], "Book One")
            self.assertEqual(reader[2][0], "Book Two")

    def test_data_path_defaults_to_data_directory(self):
        path = data_path()
        self.assertTrue(path.endswith(os.path.join("data", "books.json")))


if __name__ == "__main__":
    unittest.main()
