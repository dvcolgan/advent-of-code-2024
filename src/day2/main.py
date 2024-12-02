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
    if is_safe_increasing(report) or is_safe_decreasing(report):
        return True
    return False


def is_safe_report_with_dampening(report: Report):
    """
    For each report, check if the full report is safe.
    If not, try all combinations of reports without one
    value included.
    """

    if is_safe_report(report):
        return True

    for index_to_exclude in range(len(report)):
        for index, num in enumerate(report):
            if index == index_to_exclude:
                report2 = report.copy()
                report2.pop(index)
                if is_safe_report(report2):
                    return True
    return False


def num_safe_reports(reports: list[Report], with_dampening=False) -> int:
    count: int = 0
    for report in reports:
        if is_safe_report(report, with_dampening=with_dampening):
            count += 1
    return count


def part_1():
    reports = load_reports(config.FIXTURES_DIR / "day2" / "input.txt")
    count: int = 0
    for report in reports:
        if is_safe_report(report):
            count += 1
    print(count)


def part_2():
    reports = load_reports(config.FIXTURES_DIR / "day2" / "input.txt")
    count: int = 0
    for report in reports:
        if is_safe_report_with_dampening(report):
            count += 1
    print(count)
