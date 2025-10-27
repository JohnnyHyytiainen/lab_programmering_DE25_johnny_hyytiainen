# Kommentarer: Svenska
# Kod: Engelska
# circle.py

import math

# Decorator. Functools för att slippa upprepa mig själv med operator overloads.
# @total_ordering gör att jag enbart behöver skriva __eq__ + __lt__ (Lika med + mindre än)
# Python skapar automatiskt __le__, __gt__, __ge__ ifrån __eq__ + __lt__ med denna decorator
# Följer DRY konceptet extra mycket tack vare denna decorator.
from functools import total_ordering
from shape import Shape


@total_ordering
class Circle(Shape):
    """Circle defined by center x, y and radius > 0.

    Inherits center position (x, y) from Shape.

    Attributes:
    radius (float): Circle radius(MUST be positive)
    """

    def __init__(self, x: float | int, y: float | int, radius: float | int) -> None:
        """Initialize a circle with center and radius.

        Args:
        x (float | int) X-coordinate of center.
        y (float | int) Y-coordinate of center.
        radius (float | int) Circle radius(MUST be positive)

        Raises:
        TypeError: If any argument is not numeric.
        ValueError: If radius <= 0.
        """
        super().__init__(x, y)
        if not isinstance(radius, (int, float)):
            raise TypeError("radius must be a number")
        if radius <= 0:
            raise ValueError("radius must be > 0")
        self.radius = float(radius)

    @property
    def area(self):
        """The area of the circle (Pi * r²)

        Returns:
            Float: Area in square units.
        """
        return math.pi * self.radius**2

    @property
    def perimeter(self):
        """The perimeter of the circle (2Pi*r)

        Returns:
            float: Perimiter in linear units.
        """
        return 2 * math.pi * self.radius

    def __eq__(self, other: object) -> bool:
        """Check equality based on radius (within float tolerance)

        Args:
            other: Object to compare with.
        Returns:
            boolean: True if other is a circle with the same radius.
        """
        return isinstance(other, Circle) and math.isclose(self.radius, other.radius)
        # .isclose går att använda tack vare import math. .isclose passar perfekt att använda om jag jobbar med floats.

    def __lt__(self, other):
        return self.area < other.area if hasattr(other, "area") else NotImplemented
        # hasattr = inbyggd funktion för att kolla om objekt har en specifik attribut/metod och ger True om dom finns annars False.
        # Använder det för att förhindra AttributeError.

    def is_unit_circle(self):
        """Checks if circle is a unit circle.
        Returns:
            boolean: True if radius is approximately 1.0
        """
        return math.isclose(self.radius, 1.0)

    def __repr__(self):
        """Developer-friendly representation (recreatable)."""
        return f"Circle(x={self.x}, y={self.y}, radius={self.radius})"

    def __str__(self):
        """User-friendly string representation.

        Returns:
            str: Human-readable description of the circle.
        """
        return f"Circle at ({self.x}, {self.y}) r={self.radius}"
