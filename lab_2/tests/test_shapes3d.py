# Kommentarer: Svenska
# Kod: Engelska
# test_shapes3d.py


import pytest
from math import isclose, pi
from cube import Cube
from sphere import Sphere


def test_cube_surface_area_and_volume():
    c = Cube(0, 0, 0, 3)
    assert isclose(c.surface_area, 54.0)
    assert isclose(c.volume, 27.0)


def test_cube_equality_and_ordering():
    assert Cube(0, 0, 0, 2) < Cube(0, 0, 0, 3)
    assert Cube(1, 1, 1, 3) == Cube(5, 5, 5, 3)


def test_cube_validation():
    with pytest.raises(TypeError):
        Cube(0, 0, 0, "3")
    with pytest.raises(ValueError):
        Cube(0, 0, 0, 0)


def test_sphere_surface_area_and_volume():
    s = Sphere(0, 0, 0, 1)
    assert isclose(s.surface_area, 4 * pi)
    assert isclose(s.volume, 4 * pi / 3)


def test_sphere_equality_and_ordering():
    assert Sphere(0, 0, 0, 1) == Sphere(5, 5, 5, 1)
    assert Sphere(0, 0, 0, 1) < Sphere(0, 0, 0, 2)


def test_sphere_validation():
    with pytest.raises(TypeError):
        Sphere(0, 0, 0, "1")
    with pytest.raises(ValueError):
        Sphere(0, 0, 0, 0)
