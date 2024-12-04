from src.day4.util import get_cell, parse_board


def check_coords(board, x: int, y: int) -> bool:
    """
    M M
     A
    S S
    """
    case1 = [
        (-1, -1, "M"),
        (1, 1, "S"),
        (1, -1, "M"),
        (-1, 1, "S"),
    ]

    """
    M S
     A
    M S
    """
    case2 = [
        (-1, -1, "M"),
        (1, 1, "S"),
        (1, -1, "S"),
        (-1, 1, "M"),
    ]

    """
    S M
     A
    S M
    """
    case3 = [
        (-1, -1, "S"),
        (1, 1, "M"),
        (1, -1, "M"),
        (-1, 1, "S"),
    ]

    """
    S S
     A
    M M
    """
    case4 = [
        (-1, -1, "S"),
        (1, 1, "M"),
        (1, -1, "S"),
        (-1, 1, "M"),
    ]

    def check_case(case):
        for dx, dy, ch in case:
            if get_cell(board, x + dx, y + dy) != ch:
                return False
        return True

    # Find an A, the center of an X
    if get_cell(board, x, y) != "A":
        return False

    return any([check_case(case) for case in [case1, case2, case3, case4]])


def find_x_mas_occurrences(input: str) -> int:
    board = parse_board(input)
    count = 0

    for y in range(len(board)):
        for x in range(len(board[0])):
            if check_coords(board, x, y):
                count += 1

    return count
