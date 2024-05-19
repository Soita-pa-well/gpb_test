import unittest
from unittest.mock import patch, MagicMock
import os
import datetime
from typing import Tuple

from main import delete_files


class TestTask_4(unittest.TestCase):

    @patch('main.os.listdir')
    @patch('main.os.path.isfile')
    @patch('main.os.path.getmtime')
    @patch('main.os.remove')
    def test_delete_files(self,
                          mock_remove: MagicMock,
                          mock_getmtime: MagicMock,
                          mock_isfile: MagicMock,
                          mock_listdir: MagicMock) -> None:
        mock_listdir.return_value = ['file_1.txt', 'file_2.txt', 'file_3.txt']
        mock_isfile.side_effect = is_file

        old_time, new_time = get_time_values(31, 29)

        mock_getmtime.side_effect = [old_time, new_time, old_time]

        folder_path = 'test'
        n = 30
        delete_files(folder_path, n)

        mock_remove.assert_any_call(os.path.join(folder_path, 'file_1.txt'))
        mock_remove.assert_any_call(os.path.join(folder_path, 'file_3.txt'))
        self.assertEqual(mock_remove.call_count, 2)


def is_file(path: str) -> bool:
    return path.endswith('.txt')


def get_time_values(days_old: int, days_new: int) -> Tuple[float, float]:
    now = datetime.datetime.now()
    old_time = (now - datetime.timedelta(days=days_old)).timestamp()
    new_time = (now - datetime.timedelta(days=days_new)).timestamp()
    return old_time, new_time


if __name__ == '__main__':
    unittest.main()
