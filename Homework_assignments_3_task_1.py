# Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами.
# В результирующем списке не должно быть дубликатов.
# Пример:
# [1, 2, 3, 1, 2, 4, 5] -> [1, 2]

# Решение №1

# list_numbers = [1, 2, 3, 1, 2, 4, 5]
# new_list = []

# for number in list_numbers:
#     if list_numbers.count(number) > 1 and number not in new_list:
#         new_list.append(number)

# print(new_list)

# Решение №2

# list_numbers = [1, 2, 3, 1, 2, 4, 5]
# new_list = []
#
# for number in list_numbers:
#     if list_numbers.count(number) > 1:
#         new_list.append(number)
#
# print(list(set(new_list)))
