import unittest
from typing import List, Set

from main import (count_digits,
                  sum_digits,
                  digits_average_value,
                  tuple_trasformation)


class TestTask2(unittest.TestCase):

    def setUp(self) -> None:
        self.digits: List[Set[int]] = [{11, 3, 5}, {2, 17, 87, 32},
                                       {4, 44}, {24, 11, 9, 7, 8}]

    def test_count_digits(self) -> None:
        self.assertEqual(count_digits(self.digits), 14)

    def test_sum_digits(self) -> None:
        self.assertEqual(sum_digits(self.digits), 264)

    def test_digits_average_value(self) -> None:
        self.assertAlmostEqual(digits_average_value(self.digits), 264 / 14)

    def test_tuple_trasformation(self) -> None:
        self.assertEqual(type(tuple_trasformation(self.digits)), tuple)


if __name__ == '__main__':
    unittest.main()
