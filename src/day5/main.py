from multiprocessing import Pool
from pathlib import Path

from src import config
from src.day5.part1 import is_update_valid
from src.day5.part2 import fix_update
from src.day5.util import parse_input


def load_input(path: Path) -> str:
    return path.read_text().strip()


def middle_page(lst: list[int]) -> int:
    return lst[len(lst) // 2]


def part_1():
    rules, updates = parse_input(load_input(config.FIXTURES_DIR / "day5" / "input.txt"))
    total = 0
    for update in updates:
        if is_update_valid(rules, update):
            total += middle_page(update)

    print(total)


def calc(rules, update):
    print(f"Fixing {update}")
    return middle_page(fix_update(rules, update))


def part_2():
    rules, updates = parse_input(load_input(config.FIXTURES_DIR / "day5" / "input.txt"))
    total = 0

    with Pool() as pool:
        result = pool.starmap(
            calc,
            [
                (rules, update)
                for update in updates
                if not is_update_valid(rules, update)
            ],
        )

    print(sum(result))

    # for update in updates:
    #     if not is_update_valid(rules, update):
    #         print(f"Fixing update {update}")
    #         fixed_update = fix_update(rules, update)
    #         print(f"Fixed update {update} => {fixed_update}")
    #         total += middle_page(fixed_update)

    # print(total)
