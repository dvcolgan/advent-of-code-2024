from src import config
from src.day4.part1 import find_occurrences
from src.day4.part2 import find_x_mas_occurrences
from src.day4.util import load_input


def part_1():
    input = load_input(config.FIXTURES_DIR / "day4" / "input.txt")
    print(find_occurrences(input))


def part_2():
    input = load_input(config.FIXTURES_DIR / "day4" / "input.txt")
    print(find_x_mas_occurrences(input))
