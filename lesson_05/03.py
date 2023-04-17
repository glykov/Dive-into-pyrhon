"""
Создайте функцию генератор чисел Фибоначчи
"""


# конечная последовательность Фибоначчи
def fibonacci(n):
    prev = 0
    cur = 1
    for _ in range(n):
        yield cur
        prev, cur = cur, cur + prev


# бесконечная последовательность Фибоначчи
def fibonacci2():
    prev = 0
    cur = 1
    while True:
        yield cur
        prev, cur = cur, cur + prev


print(*fibonacci(20))

fib = fibonacci2()
for _ in range(20):
    print(next(fib), end=' ')
print()
