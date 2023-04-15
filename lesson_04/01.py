"""
Напишите функцию для транспонирования матрицы
"""


def print_matrix(matrix: list[list[int]]) -> None:
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(matrix[i][j], end=' ')
        print()


def neo(matrix: list[list[int]]) -> list[list[int]]:
    result = []
    for i in range(len(matrix[0])):
        subresult = []
        for j in range(len(matrix)):
            subresult.append(matrix[j][i])
        result.append(subresult)
    return result


matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print_matrix(matrix)
print()
print_matrix(neo(matrix))
