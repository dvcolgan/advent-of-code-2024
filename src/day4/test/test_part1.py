from unittest import TestCase

from src import config
from src.day4.part1 import check_direction, find_occurrences
from src.day4.util import get_cell, parse_board

input_path = config.FIXTURES_DIR / "day4" / "input.txt"


class Day4Tests(TestCase):
    def setUp(self):
        self.input1 = """MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX"""
        self.input2 = """....XXMAS.
.SAMXMS...
...S..A...
..A.A.MS.X
XMASAMX.MM
X.....XA.A
S.S.S.S.SS
.A.A.A.A.A
..M.M.M.MM
.X.X.XMASX"""

    def test_parse_array(self):
        self.assertListEqual(
            parse_board(self.input1),
            [
                ["M", "M", "M", "S", "X", "X", "M", "A", "S", "M"],
                ["M", "S", "A", "M", "X", "M", "S", "M", "S", "A"],
                ["A", "M", "X", "S", "X", "M", "A", "A", "M", "M"],
                ["M", "S", "A", "M", "A", "S", "M", "S", "M", "X"],
                ["X", "M", "A", "S", "A", "M", "X", "A", "M", "M"],
                ["X", "X", "A", "M", "M", "X", "X", "A", "M", "A"],
                ["S", "M", "S", "M", "S", "A", "S", "X", "S", "S"],
                ["S", "A", "X", "A", "M", "A", "S", "A", "A", "A"],
                ["M", "A", "M", "M", "M", "X", "M", "M", "M", "M"],
                ["M", "X", "M", "X", "A", "X", "M", "A", "S", "X"],
            ],
        )

    def test_get_cell(self):
        board = parse_board(self.input1)
        self.assertEqual(get_cell(board, 0, 0), "M")
        self.assertEqual(get_cell(board, 4, 4), "A")
        self.assertEqual(get_cell(board, 4, 1), "X")
        self.assertEqual(get_cell(board, 1, 4), "M")

    def test_get_cell_bounds(self):
        board = parse_board(self.input1)

        # Out of bounds gives None
        self.assertIsNone(get_cell(board, -1, 0))
        self.assertIsNone(get_cell(board, 0, -1))
        self.assertIsNone(get_cell(board, 10, 0))
        self.assertIsNone(get_cell(board, 0, 10))

        board = [[]]
        self.assertIsNone(get_cell(board, 1, 1))

    def test_check_right(self):
        board = parse_board(self.input1)
        self.assertTrue(check_direction(board, 5, 0, 1, 0))
        self.assertTrue(check_direction(board, 0, 4, 1, 0))
        self.assertTrue(check_direction(board, 5, 9, 1, 0))

        self.assertFalse(check_direction(board, 0, 5, 1, 0))

    def test_check_left(self):
        board = parse_board(self.input1)
        self.assertTrue(check_direction(board, 4, 1, -1, 0))
        self.assertTrue(check_direction(board, 6, 4, -1, 0))

        self.assertFalse(check_direction(board, 0, 5, -1, 0))

    def test_check_up(self):
        board = parse_board(self.input1)
        self.assertTrue(check_direction(board, 9, 9, 0, -1))
        self.assertTrue(check_direction(board, 6, 4, 0, -1))
        self.assertFalse(check_direction(board, 4, 4, 0, -1))

    def test_check_down(self):
        board = parse_board(self.input1)
        self.assertTrue(check_direction(board, 9, 3, 0, 1))
        self.assertFalse(check_direction(board, 6, 4, 0, 1))
        self.assertFalse(check_direction(board, 4, 4, 0, 1))

    def test_find_xmas_occurences(self):
        self.assertEqual(find_occurrences(self.input1), 18)
        self.assertEqual(find_occurrences(self.input2), 18)
