from collections.abc import Generator

# Создайте функцию генератор чисел Фибоначчи (см. Википедию).


def task_3(n: int) -> Generator[int]:
    fib_1, fib_2 = 0, 1
    for x in range(n):
        yield fib_2
        fib_1, fib_2 = fib_2, fib_1 + fib_2


for x in task_3(7):
    print(x)
