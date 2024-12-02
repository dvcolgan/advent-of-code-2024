from pathlib import Path
from typing import NewType

from src import config

Report = NewType("Report", list[int])


def load_reports(path: Path) -> list[Report]:
    reports = []
    with open(path) as f:
        for line in f:
            reports.append([int(num.strip()) for num in line.split()])

    return reports


def is_safe_increasing(report: Report):
    last_num = None
    for num in report:
        if (not last_num) or (num > last_num and num <= last_num + 3):
            last_num = num
        else:
            return False

    return True


def is_safe_decreasing(report: Report):
    last_num = None
    for num in report:
        if (not last_num) or (num < last_num and num >= last_num - 3):
            last_num = num
        else:
            return False

    return True


def is_safe_report(report: Report):
    if not (is_safe_increasing(report) or is_safe_decreasing(report)):
        return False

    return True


def num_safe_reports(reports: list[Report]) -> int:
    count: int = 0
    for report in reports:
        if is_safe_report(report):
            count += 1
    return count


def part_1():
    reports = load_reports(config.FIXTURES_DIR / "day2" / "input.txt")
    print(num_safe_reports(reports))


def part_2():
    print(0)
