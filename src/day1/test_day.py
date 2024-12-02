import subprocess
from unittest import TestCase

from src import config
from src.day1.main import load_numbers, similarity_score, total_distance

numbers_path = config.BASE_DIR / "day1" / "input.txt"


class Day1Tests(TestCase):
    def test_load_numbers_loads_numbers_into_two_lists(self):
        list1, list2 = load_numbers(numbers_path)
        self.assertIsInstance(list1, list)
        self.assertIsInstance(list2, list)
        self.assertIsInstance(list1[0], int)
        self.assertIsInstance(list2[0], int)

        lines_in_file = int(
            subprocess.run(
                f"cat {numbers_path} | wc -l",
                shell=True,
                text=True,
                capture_output=True,
                check=True,
            ).stdout
        )

        self.assertEqual(len(list1), lines_in_file)
        self.assertEqual(len(list2), lines_in_file)

    def test_total_distance_calculates_total_distance(self):
        list1 = [3, 4, 2, 1, 3, 3]
        list2 = [4, 3, 5, 3, 9, 3]
        self.assertEqual(total_distance(list1, list2), 11)

    def test_similarity_score_calculates_similarity_score(self):
        list1 = [3, 4, 2, 1, 3, 3]
        list2 = [4, 3, 5, 3, 9, 3]
        self.assertEqual(similarity_score(list1, list2), 31)

    def test_part_1_solution(self):
        list1, list2 = load_numbers(numbers_path)
        self.assertEqual(total_distance(list1, list2), 1319616)

    def test_part_2_solution(self):
        list1, list2 = load_numbers(numbers_path)
        self.assertEqual(similarity_score(list1, list2), 27267728)
