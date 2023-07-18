import json
import csv
import random
from typing import Callable

name_file = "result.csv"


def write_number_csv():
    with open(f"{name_file}", mode="w", encoding='utf-8') as w_file:
        file_writer = csv.writer(w_file, delimiter=",", lineterminator="\r")
        for i in range(random.randint(100, 1000)):
            r_1 = random.randint(1, 100)
            r_2 = random.randint(1, 100)
            r_3 = random.randint(1, 100)
            file_writer.writerow([r_1, r_2, r_3])


def json_write(funk: Callable) -> Callable:
    def wrapper(*args, **kwargs) -> None:
        rez = {f'{args}': funk(*args, **kwargs)}
        try:
            with open("result.json", "r", encoding="utf-8") as jso:
                dict_: dict = json.load(jso)
                dict_.update(rez)
                with open("result.json", "w", encoding="utf-8") as aa:
                    json.dump(dict_, aa, indent=2, ensure_ascii=False,
                              skipkeys=True)
        except FileNotFoundError:
            with open("result.json", "w", encoding="utf-8") as jso:
                json.dump(rez, jso, indent=2, ensure_ascii=False,
                          skipkeys=True)

    return wrapper


def read_csv(funk: Callable) -> Callable:
    def wrapper(*args, **kwargs) -> list:
        rez = []
        with open('aa.csv', 'r', newline='',
                  encoding='utf-8') as reader_file:
            reader_ = csv.reader(reader_file, quoting=csv.QUOTE_NONNUMERIC)
            for row in reader_:
                root = funk(*row)
                rez.append(root)
        return rez

    return wrapper


@read_csv
@json_write
def square_root(a: int | float, b: int | float,
                c: int | float) -> float | complex:
    d = b ** 2 - 4 * a * c
    if d < 0:
        d = complex(d, 0)
    x_1 = (-b + d ** .5) / (a * 2)
    x_2 = (-b - d ** .5) / (a * 2)
    if d == 0:
        return f'x = {-b / (2 * a)}'
    return f'первый корень {x_1=} второй корень {x_2=}'

write_number_csv()
square_root()
