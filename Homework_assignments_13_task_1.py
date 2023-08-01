#  Треугольник существует только тогда, когда сумма любых двух его сторон
#  больше третьей. Дано a, b, c - стороны предполагаемого треугольника.
#  Требуется сравнить длину каждого отрезка-стороны с суммой двух других.
#  Если хотя бы в одном случае отрезок окажется больше суммы двух других,
#  то треугольника с такими сторонами не существует. Отдельно сообщить
#  является ли треугольник разносторонним, равнобедренным или равносторонним.
from Error import NegativeSide, ErroneousData

class Triangle:
    def __init__(self, a: int, b: int, c: int):
        self.a = a
        self.b = b
        self.c = c
        if self.a < 0 or self.b < 0 or self.c < 0:
            raise NegativeSide(self.a, b, c)
        if self.a > self.b + self.c or self.b > self.a + self.c \
                or self.c > self.a + self.b:
            raise ErroneousData(self.a, b, c)

    def check(self):
        if self.a != self.b and self.a != self.c and self.b != self.c:
            return f"Треугольник разносторонний"
        elif self.a == self.b or self.a == self.c or self.b == self.c:
            return f"Треугольник равнобедренный"


test = Triangle(1, -1, 1)
print(test.check())