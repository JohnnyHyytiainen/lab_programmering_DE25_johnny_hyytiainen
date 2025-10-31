# Kommentarer: Svenska
# Kod: Engelska
# test_shapes2d.py

import math
import pytest
from circle import Circle
from rectangle import Rectangle


def test_rectangle_area_perimeter():
    r = Rectangle(0, 0, 2, 3)
    assert math.isclose(r.area, 6.0)
    assert math.isclose(r.perimeter, 10.0)


def test_rectangle_equality_and_ordering():
    assert Rectangle(0, 0, 2, 3) == Rectangle(5, 5, 3, 2)  # 2x3 == 3x2
    assert Rectangle(0, 0, 2, 3) > Rectangle(0, 0, 1, 1)


def test_rectangle_is_square():
    assert Rectangle(0, 0, 2, 2).is_square()


def test_rectangle_validation():
    with pytest.raises(TypeError):
        Rectangle(0, 0, "2", 3)
    with pytest.raises(ValueError):
        Rectangle(0, 0, 2, 0)
    with pytest.raises(ValueError):
        Rectangle(0, 0, -1, 2)


def test_circle_area_perimeter():
    c = Circle(0, 0, 1)
    assert math.isclose(c.area, math.pi)
    assert math.isclose(c.perimeter, 2 * math.pi)


def test_circle_equality_and_ordering():
    c1, c2 = Circle(0, 0, 1), Circle(0, 0, 2)
    assert c1 < c2
    assert Circle(10, 10, 1) == Circle(0, 0, 1)  # position ignoreras


def test_circle_validation():
    with pytest.raises(TypeError):
        Circle(0, 0, "1")
    with pytest.raises(ValueError):
        Circle(0, 0, 0)
