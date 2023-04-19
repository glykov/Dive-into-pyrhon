"""
Напишите функцию, которая принимает на вход строку —
абсолютный путь до файла. Функция возвращает кортеж из трёх
элементов: путь, имя файла, расширение файла.
"""
my_path = 'C:\\Users\\glebdom\\Documents\\hello.py'


def split_path(some_path: str) -> list:
    temp = some_path.rsplit("\\", 1)
    return (temp[0], *temp[1].split("."))


print(split_path(my_path))
