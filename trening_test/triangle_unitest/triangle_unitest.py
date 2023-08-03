import unittest
import triangle


class TestTriangle(unittest.TestCase):
    def setUp(self) -> None:
        self.triangle_versatile = triangle.Triangle(1, 2, 3)
        self.triangle_isosceles = triangle.Triangle(2, 2, 3)
        self.triangle_existence = triangle.Triangle(20, 2, 3)

    def test_versatile(self):
        self.assertEqual(self.triangle_versatile.check(),
                         'Треугольник разносторонний')

    def test_isosceles(self):
        self.assertEqual(self.triangle_isosceles.check(),
                         'Треугольник равнобедренный')

    def test_existence(self):
        self.assertEqual(self.triangle_existence.check(),
                         'Треугольника с такими сторонами не существует')

if __name__ == "__main__":
    unittest.main(verbosity=2)
