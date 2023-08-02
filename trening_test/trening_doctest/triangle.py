class Triangle:
    """
    >>> test = Triangle(1, 2, 3)
    >>> test.check()
    'Треугольник разносторонний'
    >>> test = Triangle(2, 2, 3)
    >>> test.check()
    'Треугольник равнобедренный'
    >>> test = Triangle(10, 2, 3)
    >>> test.check()
    'Треугольника с такими сторонами не существует'
    """
    def __init__(self, a: int, b: int, c: int):
        self.a = a
        self.b = b
        self.c = c

    def check(self):
        if self.a > self.b + self.c or self.b > self.a + self.c \
                or self.c > self.a + self.b:
            return f"Треугольника с такими сторонами не существует"
        elif self.a != self.b and self.a != self.c and self.b != self.c:
            return f"Треугольник разносторонний"
        elif self.a == self.b or self.a == self.c or self.b == self.c:
            return f"Треугольник равнобедренный"

