"""
Напишите следующие функции:
1. Нахождение корней квадратного уравнения
2. Генерация csv файла с тремя случайными числами в каждой строке. 100-1000 строк.
3. Декоратор, запускающий функцию нахождения корней квадратного
уравнения с каждой тройкой чисел из csv файла.
4. Декоратор, сохраняющий переданные параметры и результаты работы
функции в json файл.
"""
import math
import csv
import json
import random


def solver(func):
    def wrapper(*args, **kwargs):
        csv_reader = csv.reader(open("data.csv", "r", encoding="utf-8"))
        number = 1
        single_result = {}
        complete_results = {}
        for row in csv_reader:
            a, b, c = map(float, row)
            result = func(a, b, c)
            single_result['a'] = a
            single_result['b'] = b
            single_result['c'] = c
            single_result['result'] = [*result]
            complete_results[number] = single_result
            number += 1
        return complete_results
        
    return wrapper


def saver(func):
    def wrapper(*args, **kwargs):
        result = func(*args)
        json.dump(result, open("results.json", "w", encoding="utf-8"), indent=4, ensure_ascii=False)
    return wrapper


@saver
@solver
def solve_quadratic_equation(a: float, b: float, c: float) -> list[float]:
    d = b ** 2 - 4 * a * c
    print(d)
    if d < 0:
        return []
    x1 = (-b + math.sqrt(d)) / (a * 2)
    x2 = (-b - math.sqrt(d)) / (a * 2)
    return [x1, x2]


def generate_arguments() -> None:
    with open("data.csv", "w", encoding="utf-8", newline="") as csv_file:
        csv_writer = csv.writer(csv_file)
        for _ in range(100):
            a = random.uniform(1.0, 100.0)
            b = random.uniform(1.0, 100.0)
            c = random.uniform(1.0, 100.0)
            csv_writer.writerow([a, b, c])


if __name__ == '__main__':
    generate_arguments()
    solve_quadratic_equation(1, 1, 1)