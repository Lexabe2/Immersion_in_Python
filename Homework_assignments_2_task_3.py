# Напишите программу, которая принимает две строки вида “a/b” - дробь с
# числителем и знаменателем. Программа должна возвращать сумму и произведение*
# дробей. Для проверки своего кода используйте модуль fractions.
a = input("Введите первую дробь в формате x/x: ").split("/")
b = input("Введите вторую дробь в формате x/x: ").split("/")

product_of_fractions = f"{int(a[0]) * int(b[0])}/{int(a[1]) * int(b[1])}"

common_divisor = int(a[1]) * int(b[1])
a = f"{int(a[0]) * common_divisor // int(a[1])}/{common_divisor}"
b = f"{int(b[0]) * common_divisor // int(b[1])}/{common_divisor}"
sum_of_fractions = f"{str(int(a[0]) + int(b[0]))}/{str(common_divisor)}"

print(f"Сложение дробей: {sum_of_fractions}"
      f"\nПроизведение дробей: {product_of_fractions}")




