# В наличии текстовый файл с набором русских слов(имена существительные, им.падеж)
# Одна строка файла содержит одно слово.

# Задание:
# Написать программу которая выводит список слов, 
# каждый элемент списка которого - это новое слово,
# которое состоит из двух сцепленных в одно, которые имеются в текстовом файле.
# Порядок вывода слов НЕ имеет значения

# Например, текстовый файл содержит слова:
# ласты
# стык
# стыковка
# баласт
# кабала
# карась

# Пользователь вводмт первое слово: ласты
# Программа выводит:
# ластык
# ластыковка

# Пользователь вводмт первое слово: кабала
# Программа выводит:
# кабаласты
# кабаласт

# Пользователь вводмт первое слово: стыковка
# Программа выводит:
# стыковкабала
# стыковкарась
from typing import List


def read_words(file_path: str) -> List[str]:
    with open(file_path, 'r') as file:
        words: List[str] = [line.strip() for line in file]
    return words


def get_user_input(file_path: str) -> str:
    words: List[str] = read_words(file_path)
    while True:
        word: str = input(f'Введите слово из файла {file_path}: ').strip()
        if word in words:
            return word
        else:
            print(f'Введенное слово должно быть из файла {file_path}')


def words_transformation(path):
    res: List = []
    word: str = get_user_input(path)
    words_list: List[str] = read_words(path)

    for w in words_list:
        if w == word:
            continue

        for i in range(len(word)):
            word_part = word[i:]
            if w.startswith(word_part):
                new_word = word + w[len(word_part):]
                res.append(new_word)
                break

    return res if res else 'Нет слов, удоволетворяющих требованиям'


if __name__ == '__main__':
    file_path = 'files_for_tasks/for_task_5.txt'
    print(words_transformation(file_path))
