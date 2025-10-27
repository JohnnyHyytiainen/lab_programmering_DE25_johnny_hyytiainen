# Kommentarer: Svenska
# Kod: Engelska
# circle.py

import math

# Decorator. Functools för att slippa upprepa mig själv med operator overloads.
# Följer DRY konceptet extra mycket tack vare denna decorator.
# total_ordering gör att jag enbart behöver skriva __eq__ + __lt__ (Lika med + mindre än)
from functools import total_ordering
from shape import Shape


@total_ordering
class Circle(Shape):
    """Circle defined by center x, y and radius > 0.
    Attributes:
    x (float) center for X-coordinate.
    y (float) center for Y-coordinate.
    """

    def __init__(self, x: float | int, y: float | int, radius: float | int) -> None:
        """Validate and set the center and radius.
        Arguments:
        x (float) center X.
        y (float) center Y.

        Raises: TypeEror if any argument is not a number.
        Raises: ValueError if radius <= 0.
        """
        super().__init__(x, y)
        if not isinstance(radius, (int, float)):
            raise TypeError("radius must be a number")
        if radius <= 0:
            raise ValueError("radius must be > 0")
        self.radius = float(radius)

    @property
    def area(self):
        """Calculates the area of the circle (Pi * r2)"""
        return math.pi * self.radius**2

    @property
    def perimeter(self):
        """Calculates the perimeter of the circle (2*Pi*r)"""
        return 2 * math.pi * self.radius

    def __eq__(self, other):
        return isinstance(other, Circle) and math.isclose(self.radius, other.radius)
        # .isclose går att använda tack vare import math. .isclose passar bra att använda om jag jobbar med floats.

    def __lt__(self, other):
        return self.area < other.area if hasattr(other, "area") else NotImplemented
        # hasattr = inbyggd funktion för att kolla om objekt har en specifik attribut/metod och ger True om dom finns annars False.
        # Använder det för att förhindra AttributeError.

    def is_unit_circle(self):
        """Checks if circle is a unit circle.
        Returns True if radius is approximately 1.0
        """
        return math.isclose(self.radius, 1.0)

    def __repr__(self):
        return f"Circle(x={self.x}, y={self.y}, radius={self.radius})"

    def __str__(self):
        return f"Circle at ({self.x}, {self.y}) r={self.radius}"
