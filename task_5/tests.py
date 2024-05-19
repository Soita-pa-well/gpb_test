import unittest
from unittest.mock import patch, mock_open

from main import read_words, get_user_input, words_transformation


class TestTask5(unittest.TestCase):

    def setUp(self):
        self.words = 'ласты\nстык\nстыковка\nбаласт\nкабала\nкарась\n'
        self.file_path = 'files_for_tasks/for_task_5.txt'

    def test_read_words(self):
        with patch('builtins.open', mock_open(read_data=self.words)):
            words = read_words(self.file_path)
            self.assertEqual(words, ['ласты', 'стык', 'стыковка',
                                     'баласт', 'кабала', 'карась'])

    @patch('builtins.input', side_effect=['ласты'])
    def test_get_user_input_valid(self, mock_input):
        with patch('builtins.open', mock_open(read_data=self.words)):
            word = get_user_input(self.file_path)
            self.assertEqual(word, 'ласты')

    @patch('builtins.input', side_effect=['слово не из файла', 'ласты'])
    def test_get_user_input_fail(self, mock_input):
        with patch('builtins.open', mock_open(read_data=self.words)):
            word = get_user_input(self.file_path)
            self.assertEqual(word, 'ласты')

    @patch('main.get_user_input', return_value='ласты')
    def test_words_transformation(self, mock_get_user_input):
        with patch('builtins.open', mock_open(read_data=self.words)):
            result = words_transformation(self.file_path)
            expected_words = ['ластык', 'ластыковка']
            self.assertEqual(result, expected_words)

    @patch('main.get_user_input', return_value='Нет слов, удоволетворяющих'
                                               'требованиям')
    def test_words_transformation_fail(self, mock_get_user_input):
        with patch('builtins.open', mock_open(read_data=self.words)):
            result = words_transformation(self.file_path)
            self.assertEqual(result, 'Нет слов, удоволетворяющих требованиям')


if __name__ == '__main__':
    unittest.main()
