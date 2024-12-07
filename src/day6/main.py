from pathlib import Path
from typing import NewType

from src import config

Board = NewType("Board", list[list[int]])
Coords = NewType("Coords", tuple[int, int])

OBSTACLE = "#"
GUARD = "^"
EMPTY = "."


def load_input(path: Path) -> str:
    return path.read_text().strip()


def parse_input(raw_input: str) -> Board:
    return [list(row) for row in raw_input.split("\n")]


def clone_board(board: Board) -> Board:
    return [row[:] for row in board]


def is_out_of_bounds(board, x: int, y: int) -> bool:
    if y < 0:
        return True
    if x < 0:
        return True
    if y > len(board) - 1:
        return True
    if x > len(board[0]) - 1:
        return True

    return False


def get_cell(board: Board, x: int, y: int) -> str | None:
    if is_out_of_bounds(board, x, y):
        return None
    return board[y][x]


def find_guard(board: Board) -> Coords:
    for y in range(len(board)):
        for x in range(len(board[0])):
            cell = get_cell(board, x, y)
            if cell in ["^", ">", "<", "v"]:
                return x, y, cell
    raise ValueError("Could not find guard.")


def rotate_guard(dir: str):
    if dir == "^":
        return ">"
    elif dir == ">":
        return "v"
    elif dir == "v":
        return "<"
    elif dir == "<":
        return "^"
    else:
        raise ValueError(f"Invalid direction '{dir}'")


def get_next_step(board: Board, x: int, y: int, dir: str):
    if dir == "^":
        dx = 0
        dy = -1
    elif dir == ">":
        dx = 1
        dy = 0
    elif dir == "<":
        dx = -1
        dy = 0
    elif dir == "v":
        dx = 0
        dy = 1
    else:
        raise ValueError(f"Invalid direction '{dir}'")

    return x + dx, y + dy


def take_step(board: Board, x: int, y: int, dir: str):
    goal_x, goal_y = get_next_step(board, x, y, dir)

    # Step off board
    if is_out_of_bounds(board, goal_x, goal_y):
        return goal_x, goal_y, dir

    # Rotate at an obstacle
    goal_contents = get_cell(board, goal_x, goal_y)
    if goal_contents == "#":
        dir = rotate_guard(dir)
        return x, y, dir

    return goal_x, goal_y, dir


def print_board(board: Board, guard_x: int, guard_y: int, guard_dir: int):
    for y in range(len(board)):
        for x in range(len(board[0])):
            if guard_x == x and guard_y == y:
                print(guard_dir, end="")
            else:
                print(get_cell(board, x, y), end="")
        print()
    print()


def step_count(board: Board) -> int:
    guard_x, guard_y, guard_dir = find_guard(board)
    board[guard_y][guard_x] = "."

    distinct_coords: set[Coords] = set()
    distinct_coords.add((guard_x, guard_y))

    while True:
        guard_x, guard_y, guard_dir = take_step(board, guard_x, guard_y, guard_dir)
        # print_board(board, guard_x, guard_y, guard_dir)

        if is_out_of_bounds(board, guard_x, guard_y):
            break

        distinct_coords.add((guard_x, guard_y))

    return len(distinct_coords)


def guard_can_exit(
    board: Board,
    guard_x: int,
    guard_y: int,
    guard_dir: str,
    obstacle_x: int,
    obstacle_y: int,
) -> bool:
    distinct_coords = set()
    distinct_coords.add((guard_x, guard_y, guard_dir))

    while not is_out_of_bounds(board, guard_x, guard_y):
        guard_x, guard_y, guard_dir = take_step(board, guard_x, guard_y, guard_dir)

        new_coords = (guard_x, guard_y, guard_dir)
        if new_coords in distinct_coords:
            return False

        distinct_coords.add((guard_x, guard_y, guard_dir))

    return True


def obstacle_count(board: Board) -> int:
    guard_x, guard_y, guard_dir = find_guard(board)
    board[guard_y][guard_x] = "."

    count = 0
    for y in range(len(board)):
        for x in range(len(board[0])):
            print(x, y)
            if board[y][x] == ".":
                board[y][x] = "#"
                if not guard_can_exit(board, guard_x, guard_y, guard_dir, x, y):
                    count += 1
                board[y][x] = "."

    return count


def part_1():
    board: Board = parse_input(load_input(config.FIXTURES_DIR / "day6" / "input.txt"))
    print(step_count(board))


def part_2():
    board: Board = parse_input(load_input(config.FIXTURES_DIR / "day6" / "input.txt"))
    print(obstacle_count(board))
