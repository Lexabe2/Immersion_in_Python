import unittest
import triangle


class TestTriangle(unittest.TestCase):
    def setUp(self) -> None:
        self.triangle_versatile = triangle.Triangle(1, 2, 3)
        self.triangle_isosceles = triangle.Triangle(2, 2, 3)

    def test_comparison(self):
        self.assertEqual(self.triangle_versatile.check(),
                         'Треугольник разносторонний')
        self.assertEqual(self.triangle_isosceles.check(),
                         'Треугольник равнобедренный')


if __name__ == "__main__":
    unittest.main(verbosity=2)
