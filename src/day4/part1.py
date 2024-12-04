from src.day4.util import Board, get_cell, parse_board

SEARCH_WORD = "XMAS"


def check_direction(board: Board, x: int, y: int, dx: int, dy: int) -> bool:
    for i, ch in enumerate(SEARCH_WORD):
        if get_cell(board, x + i * dx, y + i * dy) != ch:
            return False
    return True


def check_coords(board: Board, x: int, y: int) -> bool:
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
