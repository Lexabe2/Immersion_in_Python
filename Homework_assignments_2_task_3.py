# Напишите программу, которая принимает две строки вида “a/b” - дробь с
# числителем и знаменателем. Программа должна возвращать сумму и произведение*
# дробей. Для проверки своего кода используйте модуль fractions.
a = input("Введите первую дробь в формате x/x: ")
b = input("Введите вторую дробь в формате x/x: ")

product_of_fractions = f"{int(a[0]) * int(b[0])}/{int(a[2]) * int(b[2])}"

print(f"Произведение дробей: {product_of_fractions}")

common_divisor = int(a[2]) * int(b[2])
a = f"{int(a[0]) * common_divisor // int(a[2])}/{common_divisor}"
b = f"{int(b[0]) * common_divisor // int(b[2])}/{common_divisor}"
sum_of_fractions = f"{str(int(a[0]) + int(b[0]))}/{str(common_divisor)}"

print(f"Сложение дробей: {sum_of_fractions}")
