"""
Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем. 
Программа должна возвращать сумму и произведение* дробей. 
Для проверки своего кода используйте модуль fractions.
"""
from fractions import Fraction
import math

x_num, x_denom = map(int, input("Enter a fraction (num/num): ").split("/"))
y_num, y_denom = map(int, input("Enter another fraction (num/num): ").split("/"))

x = Fraction(x_num, x_denom)
y = Fraction(y_num, y_denom)

# summing up
sum_num = x_num * y_denom + y_num * x_denom
sum_denom = x_denom * y_denom
my_gcd = math.gcd(sum_num, sum_denom)
sum_num //= my_gcd
sum_denom //= my_gcd
print(f"The sum of fractions is {sum_num}{'/' + str(sum_denom) if sum_denom != 1 else ''}")
print(f"Yes, it is correct: {x + y}")

# multiplying
prod_num = x_num * y_num
prod_denom = x_denom * y_denom
my_gcd = math.gcd(prod_num, prod_denom)
prod_num //= my_gcd
prod_denom //= my_gcd
print(f"The product of fractions is {prod_num}{'/' + str(prod_denom) if prod_denom != 1 else ''}")
print(f"Yes, it is correct: {x * y}")
