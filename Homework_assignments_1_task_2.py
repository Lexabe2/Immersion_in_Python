# Напишите программу, которая получает целое число и возвращает его 
# шестнадцатеричное строковое представление. Функцию hex используйте для 
# проверки своего результата.

number = 2000
result = ""
DIVIDER = 16

while number >= 1:
    division_result = number % DIVIDER
    if division_result == 10:
        division_result = 'A'
    elif division_result == 11:
        division_result = 'B'
    elif division_result == 12:
        division_result = 'C'
    elif division_result == 13:
        division_result = 'D'
    elif division_result == 14:
        division_result = 'E'
    elif division_result == 15:
        division_result = 'F'
    result += str(division_result)
    number = number // DIVIDER

translation = result[::-1]
print(translation)
