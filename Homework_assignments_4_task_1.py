# 1. Напишите функцию для транспонирования матрицы
# Пример:
# [[1, 2, 3], [4, 5, 6]] -> [[1,4], [2,5], [3, 6]]

def matrix(list_: list[list]) -> list[list]:
    return list(map(list, zip(*list_)))
print(matrix([[1, 2, 3], [4, 5, 6]]))
