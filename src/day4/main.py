from pathlib import Path
from typing import NewType

from src import config

Board = NewType("Board", list[list[int]])
SEARCH_WORD = "XMAS"


def load_input(path: Path) -> str:
    return path.read_text().strip()


def parse_board(input: str) -> Board:
    return [list(row) for row in input.split("\n")]


def get_cell(board: Board, x: int, y: int) -> str | None:
    if y < 0:
        return None
    if x < 0:
        return None
    if y > len(board) - 1:
        return None
    if x > len(board[0]) - 1:
        return None
    return board[y][x]


def check_direction(board, x: int, y: int, dx: int, dy: int) -> bool:
    for i, ch in enumerate(SEARCH_WORD):
        if get_cell(board, x + i * dx, y + i * dy) != ch:
            return False
    return True


def check_coords(board, x: int, y: int) -> bool:
    count = 0
    for dx, dy in [
        (0, 1),  # check right
        (0, -1),  # check left
        (-1, 0),  # check up
        (1, 0),  # check down
        (1, -1),  # check up right
        (-1, -1),  # check up left
        (-1, 1),  # check down left
        (1, 1),  # check down right
    ]:
        if check_direction(board, x, y, dx, dy):
            count += 1
    return count


def find_occurrences(input: str) -> int:
    board = parse_board(input)
    count = 0

    for y in range(len(board)):
        for x in range(len(board[0])):
            count += check_coords(board, x, y)

    return count


def part_1():
    input = load_input(config.FIXTURES_DIR / "day4" / "input.txt")
    print(find_occurrences(input))


def part_2():
    input = load_input(config.FIXTURES_DIR / "day3" / "input.txt")
    print(find_occurrences(input))
