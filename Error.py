class ErrorBase(Exception):
    pass


class NegativeSide(ErrorBase):
    def __init__(self, a: int, b: int, c: int):
        self.a = a
        self.c = c
        self.b = b
        if a < 0:
            self.status = ", сторона a отрицательная"
        elif b < 0:
            self.status = ", сторона b отрицательная"
        elif c < 0:
            self.status = ", сторона c отрицательная"

    def __str__(self):
        return f"Треугольника с отрицательными сторонами не существует{self.status}"


class ErroneousData(ErrorBase):
    def __init__(self, a: int, b: int, c: int):
        self.a = a
        self.c = c
        self.b = b
        if self.a > self.b + self.c:
            self.status = ", сторона a больше суммы сторон b и c"
        elif self.b > self.a + self.c:
            self.status = ", сторона b больше суммы сторон a и c"
        elif self.c > self.a + self.b:
            self.status = ", сторона c больше суммы сторон a и b"

    def __str__(self):
        return f"Треугольника с такими сторонами не существует{self.status}"
