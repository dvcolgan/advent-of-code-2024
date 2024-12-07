from typing import NewType

OrderingRule = NewType("OrderingRule", tuple[int, int])
UpdatePages = NewType("UpdatePages", list[int])


def parse_ordering_rule(raw_str: str) -> OrderingRule:
    fst, snd = raw_str.split("|")
    return (int(fst.strip()), int(snd.strip()))


def parse_update_pages(raw_str: str) -> UpdatePages:
    return [int(ch.strip()) for ch in raw_str.split(",")]


def parse_input(raw_str: str):
    rules = []
    updates = []
    second_half = False
    for line in raw_str.split("\n"):
        if line.strip() == "":
            second_half = True
            continue

        if not second_half:
            rules.append(parse_ordering_rule(line))
        else:
            updates.append(parse_update_pages(line))

    return rules, updates


def partition(nums: list[int], separator: int) -> tuple[list[int], list[int]]:
    i = nums.index(separator)
    return nums[:i], nums[i + 1 :]
