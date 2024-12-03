import re
from pathlib import Path

from src import config

MUL_REGEX = r"mul\((?P<num1>\d{1,3}),(?P<num2>\d{1,3})\)"
MUL_REGEX_2 = r"(do)\(\)|(don't)\(\)|(mul)\((?P<num1>\d{1,3}),(?P<num2>\d{1,3})\)"


def load_input(path: Path) -> str:
    return path.read_text()


def find_total_1(memory: str) -> list[int]:
    return sum(
        [
            int(match.group("num1")) * int(match.group("num2"))
            for match in re.finditer(MUL_REGEX, memory)
        ]
    )


def find_total_2(memory: str) -> list[int]:
    enabled = True
    total = 0
    for match in re.finditer(MUL_REGEX_2, memory):
        if match.group(1):
            enabled = True
        elif match.group(2):
            enabled = False
        elif match.group(3):
            if enabled:
                total += int(match.group("num1")) * int(match.group("num2"))

    return total


def part_1():
    memory = load_input(config.FIXTURES_DIR / "day3" / "input.txt")
    print(find_total_1(memory))


def part_2():
    memory = load_input(config.FIXTURES_DIR / "day3" / "input.txt")
    print(find_total_2(memory))
