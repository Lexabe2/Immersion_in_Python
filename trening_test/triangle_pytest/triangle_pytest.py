import pytest
from triangle import Triangle

def test_comparison():
    assert Triangle(1, 2, 3).check() == 'Треугольник разносторонний'

def test_isosceles():
    assert Triangle(2, 2, 3).check() == 'Треугольник равнобедренный'

def test_existence():
    assert Triangle(20, 2, 3).check() == 'Треугольника с такими сторонами не ' \
                                         'существует'

if __name__ == "__main__":
    pytest.main()
