from unittest import TestCase

from src import config
from src.day5.part1 import is_update_valid, partition
from src.day5.part2 import fix_update
from src.day5.util import parse_input

input_path = config.FIXTURES_DIR / "day5" / "input.txt"


class Day5Tests(TestCase):
    def setUp(self):
        self.example1 = """47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47"""

    def test_parse_input(self):
        rules, updates = parse_input(self.example1)
        self.assertListEqual(
            rules,
            [
                (47, 53),
                (97, 13),
                (97, 61),
                (97, 47),
                (75, 29),
                (61, 13),
                (75, 53),
                (29, 13),
                (97, 29),
                (53, 29),
                (61, 53),
                (97, 53),
                (61, 29),
                (47, 13),
                (75, 47),
                (97, 75),
                (47, 61),
                (75, 61),
                (47, 29),
                (75, 13),
                (53, 13),
            ],
        )
        self.assertListEqual(
            updates,
            [
                [75, 47, 61, 53, 29],
                [97, 61, 53, 29, 13],
                [75, 29, 13],
                [75, 97, 47, 61, 53],
                [61, 13, 29],
                [97, 13, 75, 29, 47],
            ],
        )

    def test_partition(self):
        all_nums = [75, 47, 61, 53, 29]

        left, right = partition(all_nums, 75)
        self.assertListEqual(left, [])
        self.assertListEqual(right, [47, 61, 53, 29])

        left, right = partition(all_nums, 61)
        self.assertListEqual(left, [75, 47])
        self.assertListEqual(right, [53, 29])

        left, right = partition(all_nums, 29)
        self.assertListEqual(left, [75, 47, 61, 53])
        self.assertListEqual(right, [])

    def test_check_update(self):
        rules, updates = parse_input(self.example1)
        self.assertTrue(is_update_valid(rules, updates[0]))
        self.assertTrue(is_update_valid(rules, updates[1]))
        self.assertTrue(is_update_valid(rules, updates[2]))
        self.assertFalse(is_update_valid(rules, updates[3]))
        self.assertFalse(is_update_valid(rules, updates[4]))
        self.assertFalse(is_update_valid(rules, updates[5]))

    def test_fix_update(self):
        rules, updates = parse_input(self.example1)
        self.assertListEqual(fix_update(rules, updates[3]), [97, 75, 47, 61, 53])
        self.assertListEqual(fix_update(rules, updates[4]), [61, 29, 13])
        self.assertListEqual(fix_update(rules, updates[5]), [97, 75, 47, 29, 13])
