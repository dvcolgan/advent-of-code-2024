from unittest import TestCase

from src import config
from src.day4.part2 import check_coords, find_x_mas_occurrences
from src.day4.util import parse_board

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
.M.S......
..A..MSMS.
.M.S.MAA..
..A.ASMSM.
.M.S.M....
..........
S.S.S.S.S.
.A.A.A.A..
M.M.M.M.M.
.........."""

    def test_check_coords(self):
        board = parse_board(self.input1)
        self.assertTrue(check_coords(board, 2, 1))
        self.assertTrue(check_coords(board, 6, 2))

    def test_find_xmas_occurences(self):
        self.assertEqual(find_x_mas_occurrences(self.input1), 9)
        self.assertEqual(find_x_mas_occurrences(self.input2), 9)
