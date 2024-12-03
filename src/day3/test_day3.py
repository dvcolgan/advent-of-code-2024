from unittest import TestCase

from src import config
from src.day3.main import (
    find_total_1,
    find_total_2,
)

input_path = config.FIXTURES_DIR / "day3" / "input.txt"


class Day3Tests(TestCase):
    def setUp(self):
        self.memory1 = (
            "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
        )
        self.memory2 = (
            "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
        )

    def test_find_total_part_1(self):
        self.assertEqual(find_total_1(self.memory1), 161)

    def test_find_total_part_2(self):
        self.assertEqual(find_total_2(self.memory2), 48)
