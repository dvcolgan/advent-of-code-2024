from pathlib import Path
from typing import NewType

Board = NewType("Board", list[list[int]])


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
