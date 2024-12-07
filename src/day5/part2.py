from src.day5.part1 import is_update_valid
from src.day5.util import OrderingRule, UpdatePages, partition

"""
This is an _extremely_ slow solution but I'm kind of invested in it at this point.
It only took 30 minutes to calculate but it got the right answer!
"""


def fix_more(rules, update):
    for page in update:
        first_rules = [rule for rule in rules if rule[0] == page]
        second_rules = [rule for rule in rules if rule[1] == page]
        before, after = partition(update, page)

        # For each rules that I am first in, if I am found to the right of any, move me to the left that one
        for i, other_page in enumerate(before):
            if any([other_page == rule[1] for rule in first_rules]):
                before.insert(i, page)
                return before + after

        # For each rules that I am second in, if I am found to the left of any, move me to the right that one
        for i, other_page in enumerate(after):
            if any([other_page == rule[0] for rule in second_rules]):
                after.insert(i + 1, page)
                return before + after


def fix_update(rules: list[OrderingRule], update: UpdatePages) -> UpdatePages:
    while not is_update_valid(rules, update):
        update = fix_more(rules, update)
    return update
