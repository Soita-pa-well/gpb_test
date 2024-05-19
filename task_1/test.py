import unittest
from unittest.mock import patch, mock_open
from main import read_csv, transform_records

RECORDS = [
            ['Фамилия1', 'Имя1', 'Отчество1', '21.11.1998', '312040348-3048'],
            ['Фамилия2', 'Имя2', 'Отчество2', '11.01.1972', '457865234-3431'],
            ['Фамилия1', 'Имя1', 'Отчество1', '21.11.1998', '312040348-3048'],
            ['Фамилия3', 'Имя3', 'Отчество3', '10.12.1990', '312040348-3048']
        ]


class TestTask4(unittest.TestCase):
    def test_read_csv(self):
        mock_data = (
            'lastname|name|patronymic|date_of_birth|id\n'
            'Фамилия1|Имя1|Отчество1|21.11.1998|312040348-3048\n'
            'Фамилия2|Имя2|Отчество2|11.01.1972|457865234-3431\n'
            'Фамилия1|Имя1|Отчество1|21.11.1998|312040348-3048\n'
            'Фамилия3|Имя3|Отчество3|10.12.1990|312040348-3048\n'
        )

        with patch('builtins.open', mock_open(read_data=mock_data)):
            records = read_csv('fake_path.csv')

        self.assertEqual(records, RECORDS)

    def test_transform_records(self):
        unique_records, duplicate_records = transform_records(RECORDS)

        unique_records = {
            '457865234-3431': ['Фамилия2', 'Имя2', 'Отчество2', '11.01.1972',
                               '457865234-3431']
        }

        duplicate_records = {
            '312040348-3048': [
                ['Фамилия1', 'Имя1', 'Отчество1', '21.11.1998',
                 '312040348-3048'],
                ['Фамилия3', 'Имя3', 'Отчество3', '10.12.1990',
                 '312040348-3048']
                 ]
        }

        self.assertEqual(unique_records, unique_records)
        self.assertEqual(duplicate_records, duplicate_records)


if __name__ == '__main__':
    unittest.main()
