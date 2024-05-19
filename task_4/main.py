# Имеется папка с файлами
# Реализовать удаление файлов старше N дней

import os
import datetime


def delete_files(folder_path: str, n: int) -> None:
    date = datetime.datetime.now() - datetime.timedelta(days=n)
    for file in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file)
        try:
            file_mod_time = datetime.datetime.fromtimestamp(os.path.getmtime(
                                                            file_path))
            if file_mod_time < date:
                os.remove(file_path)
                print(f"Файл {file} удален.")
        except Exception as e:
            print(f'Произошла ошибка {e}. {file} не является файлом')
            continue


if __name__ == '__main__':
    folder_path = 'files_for_tasks'
    N = 30
    delete_files(folder_path, N)
