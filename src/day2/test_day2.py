import subprocess
from unittest import TestCase

from src import config
from src.day2.main import (
    is_safe_decreasing,
    is_safe_increasing,
    is_safe_report,
    is_safe_report_with_dampening,
    load_reports,
)

reports_path = config.FIXTURES_DIR / "day2" / "input.txt"


class Day2Tests(TestCase):
    def test_load_reports(self):
        reports = load_reports(reports_path)
        self.assertIsInstance(reports, list)
        self.assertIsInstance(reports[0], list)
        self.assertIsInstance(reports[0][0], int)
        self.assertIsInstance(reports[0][-1], int)

        lines_in_file = int(
            subprocess.run(
                f"cat {reports_path} | wc -l",
                shell=True,
                text=True,
                capture_output=True,
                check=True,
            ).stdout
        )

        self.assertEqual(len(reports), lines_in_file)

    def test_is_safe_increasing(self):
        self.assertTrue(is_safe_increasing([1, 3, 6, 7, 9]))
        self.assertTrue(is_safe_increasing([2, 3, 4, 5, 6]))
        self.assertTrue(is_safe_increasing([3, 6, 9, 12, 15]))

        self.assertFalse(is_safe_increasing([1, 5, 9, 13, 17]))
        self.assertFalse(is_safe_increasing([1, 1, 1, 1, 1]))
        self.assertFalse(is_safe_increasing([1, 2, 2, 3, 3]))

    def test_is_safe_decreasing(self):
        self.assertTrue(is_safe_decreasing([9, 7, 6, 3, 1]))
        self.assertTrue(is_safe_decreasing([6, 5, 4, 3, 2]))
        self.assertTrue(is_safe_decreasing([15, 12, 9, 6, 3]))

        self.assertFalse(is_safe_decreasing([17, 13, 9, 5, 1]))
        self.assertFalse(is_safe_decreasing([1, 1, 1, 1, 1]))
        self.assertFalse(is_safe_decreasing([3, 3, 2, 2, 1]))

    def test_is_safe_report(self):
        test_reports = {
            "safe": [
                [7, 6, 4, 2, 1],
                [1, 3, 6, 7, 9],
            ],
            "unsafe": [
                [1, 2, 7, 8, 9],
                [9, 7, 6, 2, 1],
                [1, 3, 2, 4, 5],
                [8, 6, 4, 4, 1],
            ],
        }

        for safe_report in test_reports["safe"]:
            self.assertTrue(is_safe_report(safe_report))
        for unsafe_report in test_reports["unsafe"]:
            self.assertFalse(is_safe_report(unsafe_report))

    def test_is_safe_report_with_dampening(self):
        test_reports = {
            "safe": [
                [7, 6, 4, 2, 1],
                [1, 3, 6, 7, 9],
                [1, 3, 2, 4, 5],
                [8, 6, 4, 4, 1],
            ],
            "unsafe": [
                [1, 2, 7, 8, 9],
                [9, 7, 6, 2, 1],
            ],
        }

        for safe_report in test_reports["safe"]:
            self.assertTrue(is_safe_report_with_dampening(safe_report))
        for unsafe_report in test_reports["unsafe"]:
            self.assertFalse(is_safe_report(unsafe_report))

        self.assertTrue(is_safe_report_with_dampening([1, 4, 4, 6, 8]))
        self.assertTrue(is_safe_report_with_dampening([8, 6, 4, 4, 1]))
        self.assertTrue(is_safe_report_with_dampening([8, 6, 4, 4, 1]))
        self.assertTrue(is_safe_report_with_dampening([2, 2, 3, 4, 6]))
