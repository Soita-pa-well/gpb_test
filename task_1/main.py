# имеется текстовый файл file.csv, в котром разделитель полей с данными: | (верт. черта)
# пример ниже содержит небольшую часть этого файла(начальные 3 строки, включая строку заголовков полей)

# """
# lastname|name|patronymic|date_of_birth|id
# Фамилия1|Имя1|Отчество1 |21.11.1998   |312040348-3048
# Фамилия2|Имя2|Отчество2 |11.01.1972   |457865234-3431
# ...
# """

# Задание
# 1. Реализовать сбор уникальных записей
# 2. Случается, что под одиннаковым id присутствуют разные данные - собрать отдельно такие записи
from typing import Dict, List, Tuple


def read_csv(file_path: str) -> List[str]:
    records = []
    with open(file_path, 'r', encoding='utf-8') as file:
        next(file)
        for line in file:
            fields = line.strip().split('|')
            records.append(fields)
    records = [[field.strip() for field in record] for record in records]
    return (records)


def transform_records(records: List[List[str]]) -> Tuple[
        Dict[str, List[str]], Dict[str, List[List[str]]]]:
    unique_records: Dict[str, List[str]] = {}
    duplicate_records: Dict[str, List[str]] = {}

    for record in records:
        id = record[-1]
        if id not in unique_records:
            unique_records[id] = record
        else:
            existing_record = unique_records[id]
            if existing_record != record:
                if id not in duplicate_records:
                    duplicate_records[id] = [existing_record, record]
                else:
                    if record not in duplicate_records[id]:
                        duplicate_records[id].append(record)

    for record_id in duplicate_records:
        del unique_records[record_id]

    return unique_records, duplicate_records


if __name__ == '__main__':
    file_path = 'files_for_tasks/file.csv'
    records = read_csv(file_path)
    unique_records, duplicate_records = transform_records(records)

    print(f'Уникальные записи в файле {file_path}:')
    for record_id, record in unique_records.items():
        print(record)

    print(f'\nПовторяющиеся записи в файле {file_path}:')
    for record_id, record_list in duplicate_records.items():
        for record in record_list:
            print(record)
