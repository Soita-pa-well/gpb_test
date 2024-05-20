# Имеется банковское API возвращающее JSON
# {
# 	"Columns": ["key1", "key2", "key3"],
# 	"Description": "Банковское API каких-то важных документов",
# 	"RowCount": 2,
# 	"Rows": [
# 		["value1", "value2", "value3"],
# 		["value4", "value5", "value6"]
# 	]
# }
# Основной интерес представляют значения полей "Columns" и "Rows",
# которые соответственно являются списком названий столбцов и значениями столбцов

# Задание:
# 	1. Получить JSON из внешнего API
# 		ендпоинт: GET https://api.gazprombank.ru/very/important/docs?documents_date={"начало дня сегодня в виде таймстемп"}
# 	2. Валидировать входящий JSON используя модель pydantic
# 		(из ТЗ известно что поле "key1" имеет тип int, "key2"(datetime), "key3"(str))
# 	2. Представить данные "Columns" и "Rows" в виде плоского csv-подобного pandas.DataFrame
# 	3. В полученном DataFrame произвести переименование полей по след. маппингу
# 		"key1" -> "document_id", "key2" -> "document_dt", "key3" -> "document_name"
# 	3. Полученный DataFrame обогатить доп. столбцом:
# 		"load_dt" -> значение "сейчас"(датавремя)


# НА МОМЕНТ ВЫПРОЛНЕНИЯ ЗАДАНИЯ (19.05 - 20.05), УКАЗАННЫЙ В ТЗ ЭНДПОИНТ НЕ ОТВЕЧАЛ.

import requests
import datetime
import time
from typing import List, Dict

from pydantic import ValidationError

from models import Columns
from dataframes import add_column


def get_data() -> Dict:
    url = f'https://api.gazprombank.ru/very/important/docs?documents_date={get_timestamp()}'
    response = requests.get(url)
    response.raise_for_status()
    return response.json()


def get_timestamp() -> int:
    now = datetime.datetime.now()
    start_of_day = datetime.datetime(now.year, now.month, now.day)
    timestamp = int(time.mktime(start_of_day.timetuple()))
    return timestamp


def validate_data(data: Dict) -> List[Columns]:
    documents = []
    if 'Columns' in data and isinstance(data['Columns'], list):
        for value in data['Columns']:
            try:
                document = Columns(
                    key1=value[0],
                    key2=datetime.datetime.strptime(
                        value[1], '%Y-%m-%dT%H:%M:%S'),
                    key3=value[2]
                )
                documents.append(document)
            except ValidationError as e:
                print(f'Validation error: {e}')
            except (IndexError, ValueError) as e:
                print(f'Ошибка : {e}')
    return documents


if __name__ == '__main__':
    print(add_column())
