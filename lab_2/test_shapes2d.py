# Kommentarer: Svenska
# Kod: Engelska
# test_shapes2d.py

from math import pi, isclose
from circle import Circle
from rectangle import Rectangle

assert Circle(0, 0, 1) == Circle(10, 10, 1)
assert Rectangle(0, 0, 2, 3) == Rectangle(5, 5, 3, 2)
assert Circle(0, 0, 3) > Circle(0, 0, 1)
assert Rectangle(0, 0, 2, 3) > Rectangle(0, 0, 1, 1)
assert Circle(0, 0, 1).is_unit_circle() is True
assert Rectangle(0, 0, 2, 2).is_square() is True
c = Circle(0, 0, 2)
assert isclose(c.area, pi * 4) and isclose(c.perimeter, 2 * pi * 2)
try:
    Circle(0, 0, 0)
    assert False
except ValueError:
    pass
try:
    Rectangle(0, 0, 1, "h")
    assert False
except TypeError:
    pass
try:
    r = Rectangle(0, 0, 1, 2)
    r.translate("X", 1)
    assert False
except TypeError:
    pass

assert Rectangle(0, 0, 2, 3) == Rectangle(5, 5, 3, 2)
assert Rectangle(0, 0, 2, 3) > Rectangle(0, 0, 1, 1)
assert Rectangle(0, 0, 2, 2).is_square() is True
try:
    Rectangle(0, 0, 1, "h")
    assert False
except TypeError:
    pass
try:
    Rectangle(0, 0, -1, 2)
    assert False
except ValueError:
    pass
