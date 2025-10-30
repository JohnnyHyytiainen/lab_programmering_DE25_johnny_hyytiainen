# Kommentarer: Svenska
# Kod: Engelska
# manual_test.py


from math import pi, isclose
from circle import Circle
from rectangle import Rectangle
from sphere import Sphere
from cube import Cube


# 2d shapes. Rektangel och cirkel
print("--- 2D Circle and Rectangle ---")
circle1 = Circle(x=0, y=0, radius=1)  # enhetcirkel
circle2 = Circle(x=1, y=1, radius=1)
rectangle1 = Rectangle(x=0, y=0, width=1, height=1)

print("circle1 == circle2 ?", circle1 == circle2)  # True (samma radie)
print("circle2 == rectangle1 ?", circle2 == rectangle1)  # False (olika typer)

print("\n-- translate and errors --")
print(f"before: circle1 at ({circle1.x},{circle1.y})")
circle1.translate(5, 3)
print(f"after : circle1 at ({circle1.x},{circle1.y})")
try:
    circle1.translate("THREE", 5)
except TypeError as e:
    print("caught TypeError (translate)", e)

print("\n-- ordering and props --")
circle3 = Circle(x=0, y=0, radius=3)  # center (0,0)
print("circle3 >= circle1 ?", circle3 >= circle1)  # True
print("circle3 area ~ 9pi ?", isclose(circle3.area, 9 * pi))
print("rectangle1 perimeter =", rectangle1.perimeter)

print("\n-- rectangle equality (2×3 == 3×2) --")
rectangle2 = Rectangle(x=5, y=5, width=3, height=2)
print("rectangle1 == rectangle2 ?", rectangle1 == rectangle2)  # False (1×1 vs 3×2)
rectangle3 = Rectangle(x=0, y=0, width=2, height=3)
rectangle4 = Rectangle(x=0, y=0, width=3, height=2)
print("2×3 == 3×2 ?", rectangle3 == rectangle4)  # True
print("is_square(1×1) ?", rectangle1.is_square())  # True

try:
    Rectangle(x=0, y=0, width=3, height="5")
except TypeError as e:
    print("caught TypeError (constructor):", e)

# 3d shapes, kub och sfär

print("\n--- 3D Sphere and Cube ---")
s = Sphere(0, 0, 0, 1)
c = Cube(2, 0, 0, 3)
print("sphere surface area ~ 4pi ?", isclose(s.surface_area, 4 * pi))
print("sphere volume ~ 4/3 pi ?", isclose(s.volume, 4 * pi / 3))
print("cube surface area =", c.surface_area, "cube volume =", c.volume)
print(f"sphere moved to ({s.x},{s.y},{s.z})")
try:
    Cube(0, 0, 0, "a")
except TypeError as e:
    print("caught TypeError (cube)", e)
