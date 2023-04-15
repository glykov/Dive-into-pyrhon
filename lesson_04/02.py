"""
Напишите функцию принимающую на вход только ключевые
параметры и возвращающую словарь, где ключ — значение
переданного аргумента, а значение — имя аргумента. Если
ключ не хешируем, используйте его строковое представление.
"""
import pprint
from collections.abc import Hashable

def make_dict(**kwargs) -> dict:
    result = {}
    for k, v in kwargs.items():
        if not isinstance(v, Hashable):
            v = str(v) 
        result[v] = k
    return result


pprint.pprint(make_dict(one=[1, 1, 1], two=2, three="oops"))