from rectangle import Rectangle

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
