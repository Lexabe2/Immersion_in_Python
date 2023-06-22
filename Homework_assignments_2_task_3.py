# Напишите программу, которая принимает две строки вида “a/b” - дробь с 
# числителем и знаменателем. Программа должна возвращать сумму и произведение* 
# дробей. Для проверки своего кода используйте модуль fractions.
a = "1/2"
b = "1/3"

product_of_fractions = f"{int(a[0]) * int(b[0])}/{int(a[2]) * int(b[2])}"

print(product_of_fractions)

common_divisor = int(a[2]) * int(b[2])
a = f"{int(a[0]) * common_divisor // int(a[2])}/{common_divisor}"
b = f"{int(b[0]) * common_divisor // int(b[2])}/{common_divisor}"
sum_of_fractions = f"{str(int(a[0]) + int(b[0]))}/{str(common_divisor)}"

print(sum_of_fractions)
