"""
Возьмите задачу о банкомате из семинара 2. Превратите функции в методы класса, а
параметры в свойства. Задачи должны решаться через вызов методов
экземпляра.
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

class Atm:
    def __init__(self):
        self.total_amount = 0
        self.operation_counter = 0


    def get_amount(self) -> int:
        amount = int(input("Enter the amount for operation: "))
        while amount % 50 != 0:
            amount = int(input("Amount must be multiple of 50. Try again: "))
        return amount


    def check_total_amount(self) -> None:
        if self.total_amount > 5_000_000:
            self.total_amount *= 0.9


    def check_operation_count(self) -> None:
        if self.operation_counter % 3 == 0:
            self.total_amount *= 1.03


    def print_total_amount(self) -> None:
        print(f'You have {self.total_amount}')


    def deposit(self):
        self.operation_counter += 1
        self.check_total_amount()
        amount = self.get_amount()
        self.total_amount += amount
        self.check_operation_count()
        self.print_total_amount()


    def withdraw(self):
        self.operation_counter += 1
        self.check_total_amount()
        amount = self.get_amount()
        if amount > self.total_amount:
            print("You cannot withdraw more money than you have")
        else:
            self.total_amount -= amount
            self.total_amount -= self.total_amount * 0.015
        self.check_operation_count()
        self.print_total_amount()

if __name__ == '__main__':
    atm = Atm()
    user_choice = 0
    while user_choice != 3:
        print('Choose what you want to do:\n1. deposit\n2. withdraw\n3. exit')
        user_choice = int(input())
        match user_choice:
            case 1: atm.deposit()
            case 2: atm.withdraw()
            case 3: break
            case _: print("illegal operation")