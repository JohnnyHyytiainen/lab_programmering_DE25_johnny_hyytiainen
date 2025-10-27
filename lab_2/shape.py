# Kommentarer: Svenska
# Kod: Engelska
# shape.py


"""Abstract base for shapes with a center point and translation.
Provides the contract for read-only 'area' and 'perimeter' properties.
"""

from abc import ABC, abstractmethod


class Shape(ABC):
    """
    An abstract base class for a geometric shape with a center position.

    Attributes:
        x (float) X-coordinate of the shapes center.
        y (float) Y-coordinate of the shapes center.

    Invariants:
        x and y are finite real numbers.
    """

    # Validera typer och normalisera till float för aritmetik

    def __init__(self, x, y):
        if not isinstance(x, (int, float)):
            raise TypeError("x must be a number, not {type(x).__name__}")
        if not isinstance(y, (int, float)):
            raise TypeError("y must be a number, not {type(y).__name__}")
        # Alltid lagra som float för konsekvent datatyp
        self.x = float(x)
        self.y = float(y)

    def translate(self, dx: float | int, dy: float | int) -> None:
        """Move the shapes center by (dx, dy)

        Args:
            dx (float or int) The distance to move along the x axis.
            dy (float or int) The distance to move along the y axis.

        Raises:
            TypeError: If dx or dy are not numeric.
        """
        # TypeError "vakt" om x/y/dx/dy inte är giltigt värde, som en string
        if not isinstance(dx, (int, float)) or not isinstance(dy, (int, float)):
            raise TypeError("dx, dy must be numbers")
        self.x += float(dx)
        self.y += float(dy)

    @property
    @abstractmethod
    def area(self) -> float:
        """Read only geometric area of the shape"""
        raise NotImplementedError

    @property
    @abstractmethod
    def perimeter(self) -> float:
        """Read only perimeter/circumference of the shape"""
        raise NotImplementedError
