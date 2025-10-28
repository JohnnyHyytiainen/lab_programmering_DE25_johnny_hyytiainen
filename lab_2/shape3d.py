# Kommentarer: Svenska
# Kod: Engelska
# shape3d.py

"""Abstract base for 3D shapes with a center point (x,y,z) and translation.
   Provides the contract for read only 'volume' and 'surface_area' properties.
"""

# abc = standard bibliotek, ABC = basklass, abstractmethod = decorator
# @abstractmethod "tvingar" child klasserna att använda samma method. Gör det för att få alla child klasser att följa samma regler
from abc import ABC, abstractmethod


class Shape3D(ABC):
    """
    Abstract base class for 3D shapes with a center position (x, y, z).

    Attributes:
        x (float): Center x-coordinate.
        y (float): Center y-coordinate.
        z (float): Center z-coordinate.
    """

    def __init__(self, x: float | int, y: float | int, z: float | int):
        """
        Initializes the 3D shapes center coordinates.

        Args:
            x (float | int): X-coordinate of center.
            y (float | int): Y-coordinate of center.
            z (float | int): Z-coordinate of center.

        Raises:
            TypeError: If x, y, or z-coordinates are not numeric.
        """
        for name, value in (("x", x), ("y", y), ("z", z)):
            if not isinstance(value, (int, float)):
                # TypeError "vakt" om x/y/z inte är giltigt värde, som en string(Samma logik som shape.py)
                raise TypeError(f"{name} must be a number!")
        # Alltid lagra som float för konsekvent datatyp som i shape.py
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)

    def translate(self, dx: float | int, dy: float | int, dz: float | int) -> None:
        """
        Move the shapes center by dx, dy, dz.

        Raises:
            TypeError: If dx, dy or dz are not numeric.
        """
        for name, value in (("dx", dx), ("dy", dy), ("dz", dz)):
            if not isinstance(value, (int, float)):
                # TypeError "vakt" om dx/dy/dz inte är giltigt värde, som en string(Samma logik som shape.py)
                raise TypeError(f"{name} must be a number!")

        self.x += float(dx)
        self.y += float(dy)
        self.z += float(dz)

    # @property decorator istället för att använda mig utav getter funktion för Shape3D
    # @property gör mina värden read-only
    # Följa DRY konceptet
    @property
    @abstractmethod
    def volume(self) -> float:
        """Read only property: The volume of the 3D shape."""
        raise NotImplementedError

    # @property decorator istället för att använda mig utav getter funktion för Shape3D
    # @property gör mina värden read-only
    # Följa DRY konceptet
    @property
    @abstractmethod
    def surface_area(self) -> float:
        """Read only property: The surface area of the 3D shape."""
        raise NotImplementedError
