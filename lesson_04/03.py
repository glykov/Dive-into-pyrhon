"""
Возьмите задачу о банкомате из семинара 2. Разбейте её
на отдельные операции — функции. Дополнительно сохраняйте
все операции поступления и снятия средств в список.
Напишите программу банкомат.
✔ Начальная сумма равна нулю
✔ Допустимые действия: пополнить, снять, выйти
✔ Сумма пополнения и снятия кратны 50 у.е.
✔ Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
✔ После каждой третей операции пополнения или снятия начисляются проценты - 3%
✔ Нельзя снять больше, чем на счёте
✔ При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой
операцией, даже ошибочной
✔ Любое действие выводит сумму денег
"""
total_amount = 0
operation_counter = 0


def get_amount() -> int:
    amount = int(input("Enter the amount for operation: "))
    while amount % 50 != 0:
        amount = int(input("Amount must be multiple of 50. Try again: "))
    return amount


def check_total_amount() -> None:
    global total_amount
    if total_amount > 5_000_000:
        total_amount *= 0.9


def check_operation_count() -> None:
    global operation_counter, total_amount
    if operation_counter % 3 == 0:
        total_amount *= 1.03


def print_total_amount() -> None:
    global total_amount
    print(f'You have {total_amount}')


def deposit():
    global total_amount, operation_counter
    operation_counter += 1
    check_total_amount()
    amount = get_amount()
    total_amount += amount
    check_operation_count()
    print_total_amount()


def withdraw():
    global total_amount, operation_counter
    operation_counter += 1
    check_total_amount()
    amount = get_amount()
    if amount > total_amount:
        print("You cannot withdraw more money than you have")
    else:
        total_amount -= amount
        total_amount -= total_amount * 0.015
    check_operation_count()
    print_total_amount()

if __name__ == '__main__':
    user_choice = 0
    while user_choice != 3:
        print('Choose what you want to do:\n1. deposit\n2. withdraw\n3. exit')
        user_choice = int(input())
        match user_choice:
            case 1: deposit()
            case 2: withdraw()
            case 3: break
            case _: print("illegal operation")