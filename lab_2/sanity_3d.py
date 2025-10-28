from math import pi, isclose
from cube import Cube
from sphere import Sphere

# Cube sanity check
c1 = Cube(0, 0, 0, 3)
c2 = Cube(1, 1, 1, 3)
c3 = Cube(0, 0, 0, 2)

assert isclose(c1.surface_area, 54.0)
assert isclose(c1.volume, 27.0)
assert c1 == c2  # samma sidlängd, position ignoreras
assert c3 < c1  # volymordning

try:
    Cube(0, 0, 0, 0)
    assert False
except ValueError:
    pass
try:
    Cube(0, 0, 0, "a")
    assert False
except TypeError:
    pass
try:
    t = Cube(0, 0, 0, 1)
    t.translate("dx", 0, 0)
    assert False
except TypeError:
    pass

# Sphere sanity check


s1 = Sphere(0, 0, 0, 1)
s2 = Sphere(2, 2, 2, 1)
s3 = Sphere(0, 0, 0, 2)
assert isclose(s1.surface_area, 4 * pi)
assert isclose(s1.volume, 4 * pi / 3)
assert s1 == s2  # likhet: radius, position ignoreras
assert s1 < s3  # ordning: volym

c = Cube(0, 0, 0, 3)
assert c > s1  # blandad sortering via volume funkar
s1.translate(1, -1, 2)
assert (s1.x, s1.y, s1.z) == (1.0, -1.0, 2.0)
assert not (s1 == c)  # sphere vs cube ska vara False

try:
    Sphere(0, 0, 0, 0)
    assert False
except ValueError:
    pass
try:
    t = Sphere(0, 0, 0, 1)
    t.translate("dx", 0, 0)
    assert False
except TypeError:
    pass
