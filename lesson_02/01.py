"""
Напишите программу, которая получает целое число и 
возвращает его шестнадцатеричное строковое представление. 
Функцию hex используйте для проверки своего результата.
"""

symbols = "0123456789ABCDEF"
result = ""
num = int(input("Enter a number: "))

print(hex(num))

while num:
    digit = num % 16
    result = symbols[digit] + result
    num //= 16

print("0x" + result)
