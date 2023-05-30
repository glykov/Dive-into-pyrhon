"""
Создайте класс Матрица. Добавьте методы для:
○ вывода на печать,
○ сравнения,
○ сложения,
○ *умножения матриц
"""
import random


class Matrix:
    '''
    Класс для работы с матрицами
    '''

    def __init__(self, rows, cols):
        ''' Инициализация матрицы заданных размеров '''

        self.matrix = [0] * rows
        for i in range(rows):
            self.matrix[i] = [0] * cols

    def fill_matrix_rand(self):
        ''' Заполнение матрицы случайными числами от 1 до 10 '''

        for row in range(len(self.matrix)):
            for col in range(len(self.matrix[row])):
                self.matrix[row][col] = random.randint(1, 10)

    def print_matrix(self):
        ''' Вывод матрицы на печать '''

        for row in self.matrix:
            for col in row:
                print(f'{col:^3}', end='')
            print()

    def __eq__(self, other):
        ''' Сравнение двух матриц поэлементно '''

        if len(self.matrix) != len(other.matrix):
            return False
        for i in range(len(self.matrix)):
            if len(self.matrix[i]) != len(other.matrix[i]):
                return False
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                if self.matrix[i][j] != other.matrix[i][j]:
                    return False
        return True

    def __lt__(self, other):
        ''' Сравнение двух матриц поэлементно '''

        if len(self.matrix) >= len(other.matrix):
            return False
        for i in range(len(self.matrix)):
            if len(self.matrix[i]) >= len(other.matrix[i]):
                return False
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                if self.matrix[i][j] >= other.matrix[i][j]:
                    return False
        return True

    def __le__(self, other):
        ''' Сравнение двух матриц поэлементно '''

        if len(self.matrix) > len(other.matrix):
            return False
        for i in range(len(self.matrix)):
            if len(self.matrix[i]) > len(other.matrix[i]):
                return False
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                if self.matrix[i][j] > other.matrix[i][j]:
                    return False
        return True

    def __add__(self, other):
        if (len(self.matrix) != len(other.matrix)):
            return None
        result = Matrix(len(self.matrix), len(self.matrix[0]))
        for i in range(len(self.matrix)):
            if (len(self.matrix[i]) != len(other.matrix[i])):
                return None
            for j in range(len(self.matrix[i])):
                result.matrix[i][j] = self.matrix[i][j] + other.matrix[i][j]
        return result


if __name__ == '__main__':
    A = Matrix(3, 3)
    B = Matrix(3, 3)

    A.fill_matrix_rand()
    A.print_matrix()
    print()

    B.fill_matrix_rand()
    B.print_matrix()
    print()

    C = A + B
    C.print_matrix()
