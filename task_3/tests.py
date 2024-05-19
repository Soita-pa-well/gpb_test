import unittest
from typing import List, Dict

from main import dict_transformation


class TestTask3(unittest.TestCase):

    def setUp(self) -> None:
        self.digits: List[List[int]] = [[1, 2, 3], [4, 5, 6]]

    def test_dict_transformation(self) -> None:
        result: List[Dict[str, int]] = [{'k1': 1, 'k2': 2, 'k3': 3},
                                        {'k1': 4, 'k2': 5, 'k3': 6}]
        self.assertEqual(dict_transformation(self.digits), result)


if __name__ == '__main__':
    unittest.main()
