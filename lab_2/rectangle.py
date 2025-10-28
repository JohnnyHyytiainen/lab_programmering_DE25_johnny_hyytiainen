# Kommentarer: Svenska
# Kod: Engelska
# rectangle.py

import math

# Decorator. Functools för att slippa upprepa mig själv med operator overloads.
# @total_ordering gör att jag enbart behöver skriva __eq__ + __lt__ (Lika med + mindre än)
# Python skapar automatiskt __le__, __gt__, __ge__ ifrån __eq__ + __lt__ med denna decorator
# Följer DRY konceptet extra mycket tack vare denna decorator.
from functools import total_ordering
from shape import Shape


@total_ordering
class Rectangle(Shape):
    """Rectangle defined by center (x, y) and positive width and height.

    Attributes:
        x (float): Center x-coordinate(inherited from Shape).
        y (float): Center y-coordinate(inherited from Shape).
        width (float): Side length along x (>0).
        height (float): Side length along y (>0).

    Invariants:
     - width > 0 and height > 0
    """

    def __init__(self, x: float, y: float, width: float, height: float):
        """Validate and set center and length of sides.

        Args:
            x (float): Center x-coordinate.
            y (float): Center y-coordinate.
            width(float): Width (>0).
            height(float): Height (>0).

        Raises:
            TypeError: If any argument is not a number.
            ValueError: if width <= 0 or height <= 0.
        """
        super().__init__(x, y)
        # Typkolla först, släng tidigt för att underlätta felsökning.
        if not isinstance(width, (int, float)):
            raise TypeError("Width must be a number!")
        if not isinstance(height, (int, float)):
            raise TypeError("Height must be a number!")
        if width <= 0:
            raise ValueError("Width must be > 0!")
        if height <= 0:
            raise ValueError("Height must be > 0!")
        # Normalisera till float för mer konsekvent matte.
        self.width = float(width)
        self.height = float(height)

    @property
    def area(self):
        """Read only property. The area of the rectangle (width*height)."""
        return self.width * self.height

    @property
    def perimeter(self):
        """Read only property: The perimeter of the rectangle 2*(width + height)."""
        return 2 * (self.width + self.height)

    def __eq__(self, other: object) -> bool:
        """
        Checks for equality with another object.

        Returns:
            Bool: True if "other" is a Rectangle and they have the same dimensions.
        """
        if not isinstance(other, Rectangle):
            return False
        # Likhet = mått och inte position. Tillåter byte av sidor
        # Jämför dimensioner med tolerans pga floats
        w1, h1 = self.width, self.height
        w2, h2 = other.width, other.height

        # Ser om de är lika (w1==w2, h1==h2)
        # Likhet = mått och inte position. Tillåter byte av sidor(w1==h2, h1==w2)
        return (math.isclose(w1, w2) and math.isclose(h1, h2)) or (
            math.isclose(w1, h2) and math.isclose(h1, w2)
        )
        # .isclose går att använda tack vare import math. .isclose passar perfekt att använda om jag jobbar med floats.

    def __lt__(self, other: object) -> bool:
        """Compares this rectangle to another shape based on area."""
        return self.area < other.area if hasattr(other, "area") else NotImplemented
        # hasattr = inbyggd funktion för att kolla om objekt har en specifik attribut/metod och ger True om dom finns annars False.
        # Använder det för att förhindra AttributeError.

    def is_square(self) -> bool:
        """Return True if width and height are approximately equal"""
        return math.isclose(self.width, self.height)

    def __repr__(self) -> str:
        """Developer-friendly, recreatable representation."""
        return f"Rectangle(x={self.x}, y={self.y}, width={self.width}, height={self.height})"

    def __str__(self) -> str:
        """User-friendly string representation.

        Returns:
            str: Human-readable description of the circle.
        """
        return f"Rectangle at ({self.x}, {self.y}) {self.width}×{self.height}"
