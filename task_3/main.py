# имеется список списков
# a = [[1,2,3], [4,5,6]]
# Задание:
# сделать список словарей
# b = [{'k1': 1, 'k2': 2, 'k3': 3}, {'k1': 4, 'k2': 5, 'k3': 6}]
# *написать решение в одну строку

from typing import List, Dict


def dict_transformation(digits_list: List[List[int]]) -> List[Dict[str, int]]:
    return [dict(zip(['k1', 'k2', 'k3'], nested_list))
            for nested_list in digits_list]


if __name__ == '__main__':
    a = [[1, 2, 3], [4, 5, 6]]
    print(dict_transformation(a))
