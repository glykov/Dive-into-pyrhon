number = int(input('Введите натуральное число больше 1: '))

is_prime = True
divisor = 2
while divisor * divisor <= number:
    if number % divisor == 0:
        is_prime = False
        break
    divisor += 1

print(f'Число {number} - {"не " if not is_prime else ""}является простым')