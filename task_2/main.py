# в наличии список множеств. внутри множества целые числа
# m = [{11, 3, 5}, {2, 17, 87, 32}, {4, 44}, {24, 11, 9, 7, 8}]
# Задание: посчитать
#  1. общее количество чисел
#  2. общую сумму чисел
#  3. посчитать среднее значение
#  4. собрать все множества в один кортеж
# *написать решения в одну строку

from typing import List, Set, Tuple


def count_digits(digits_list: List[Set[int]]) -> int:
    return sum(len(nested_set) for nested_set in digits_list)


def sum_digits(digits_list: List[Set[int]]) -> int:
    return sum(digit for nested_set in digits_list for digit in nested_set)


def digits_average_value(digits_list: List[Set[int]]) -> float:
    return sum_digits(digits_list) / count_digits(digits_list)


def tuple_trasformation(digits_list: List[Set[int]]) -> Tuple[Set[int]]:
    return tuple((nested_set) for nested_set in digits_list)


if __name__ == '__main__':
    m = [{11, 3, 5}, {2, 17, 87, 32}, {4, 44}, {24, 11, 9, 7, 8}]
    print(f'Количество чисел в коллекции: {count_digits(m)}')
    print(f'Результат сложения чисел в коллекции: {sum_digits(m)}')
    print(f'Cреднее значение чисел в коллекции: {digits_average_value(m)}')
    print(
        f'Результат превращения коллекции в структуру данных '
        f'{type(tuple_trasformation(m))}: {tuple_trasformation(m)}'
    )
