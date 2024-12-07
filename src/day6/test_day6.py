from unittest import TestCase

from src.day6.main import (
    clone_board,
    find_guard,
    obstacle_count,
    parse_input,
    step_count,
)


class Day6Tests(TestCase):
    def setUp(self):
        self.example1 = """....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#..."""
        self.board1 = parse_input(self.example1)

    def test_parse_input(self):
        self.assertListEqual(
            self.board1,
            [
                [".", ".", ".", ".", "#", ".", ".", ".", ".", "."],
                [".", ".", ".", ".", ".", ".", ".", ".", ".", "#"],
                [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
                [".", ".", "#", ".", ".", ".", ".", ".", ".", "."],
                [".", ".", ".", ".", ".", ".", ".", "#", ".", "."],
                [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
                [".", "#", ".", ".", "^", ".", ".", ".", ".", "."],
                [".", ".", ".", ".", ".", ".", ".", ".", "#", "."],
                ["#", ".", ".", ".", ".", ".", ".", ".", ".", "."],
                [".", ".", ".", ".", ".", ".", "#", ".", ".", "."],
            ],
        )

    def test_clone_board(self):
        board2 = clone_board(self.board1)
        self.assertListEqual(self.board1, board2)
        self.assertIsNot(self.board1, board2)

    def test_step_count(self):
        count = step_count(self.board1)
        self.assertEqual(count, 41)

    def test_find_guard(self):
        self.assertTupleEqual(find_guard(self.board1), (4, 6, "^"))

    def test_obstacle_count(self):
        count = obstacle_count(self.board1)
        self.assertEqual(count, 6)
