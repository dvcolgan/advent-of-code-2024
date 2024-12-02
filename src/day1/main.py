from pathlib import Path

from src.config import BASE_DIR


def load_numbers(path: Path) -> tuple[list[int], list[int]]:
    list1 = []
    list2 = []
    with open(path) as f:
        for line in f:
            num1, num2 = line.split()

            num1 = int(num1.strip())
            num2 = int(num2.strip())
            list1.append(num1)
            list2.append(num2)
    return list1, list2


def total_distance(list1: list[int], list2: list[int]):
    sorted1 = sorted(list1)
    sorted2 = sorted(list2)
    dist = 0
    for num1, num2 in zip(sorted1, sorted2):
        dist += abs(max(num1, num2) - min(num1, num2))
    return dist


def main():
    numbers_path = BASE_DIR / "day1" / "input.txt"
    list1, list2 = load_numbers(numbers_path)
    dist = total_distance(list1, list2)
    print(dist)
