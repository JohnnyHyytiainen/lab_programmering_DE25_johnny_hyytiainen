# Kommentarer: Svenska
# Kod: Engelska
# cube.py


# Decorator. Functools för att slippa upprepa mig själv med operator overloads.
# @total_ordering gör att jag enbart behöver skriva __eq__ + __lt__ (Lika med + mindre än)
# Python skapar automatiskt __le__, __gt__, __ge__ ifrån __eq__ + __lt__ med denna decorator
# Följer DRY konceptet extra mycket tack vare denna decorator.
from functools import total_ordering
from shape3d import Shape3D
import math


@total_ordering
class Cube(Shape3D):
    """
    A Cube, defined by a center point (x,y,z) and a side length.
    Inherits (x,y,z) and translate from Shape3D.
    """

    def __init__(
        self, x: float | int, y: float | int, z: float | int, side: float | int
    ):
        """Initializes the cube.

        Args:
            x,y,z (float | int): Center coordinates
            side (float | int): Side length must be > 0.

        Raises:
            TypeError: If any argument is not numeric.
            ValueError: If side <= 0.

        """
        # skicka x,y,z till parent class(Shape3D)
        super().__init__(x, y, z)
        # hanterar enbart det som är unikt för Cube klassen
        if not isinstance(side, (int, float)):
            raise TypeError("side must be a number!")
        if side <= 0:
            raise ValueError("side must be > 0")
        self.side = float(side)

    # @property decorator istället för att använda mig utav getter funktion för Shape3D
    # @property gör mina värden read-only
    # Följa DRY konceptet
    @property
    def surface_area(self) -> float:
        """The surface area of the cube (6*side^2)"""
        return 6 * self.side**2

    # Samma som ovan
    @property
    def volume(self) -> float:
        """The volume of the cube (Side^3)"""
        return self.side**3

    # Två operators behövs för att total_ordering decoratorn ska bli användbar == DRY
    # (__eq__ + __lt__ behövs för detta. Lika med + mindre än)
    # kub1 == kub2 om kub1 och kub2 har samma sidlängd
    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Cube):
            return False
        return math.isclose(self.side, other.side)
        # .isclose går att använda tack vare import math. .isclose passar perfekt att använda om jag jobbar med floats.

    # Operator nr 2. Jämför kub1 och kub2 baserat på deras volym
    def __lt__(self, other: object) -> bool:
        if not hasattr(other, "volume"):
            return NotImplemented
        return self.volume < other.volume
        # hasattr = inbyggd funktion för att kolla om objekt har en specifik attribut/metod och ger True om dom finns annars False.
        # Använder det för att förhindra AttributeError.

    def __repr__(self) -> str:
        """Developer-friendly representation (recreatable)."""
        return f"Cube(x={self.x}, y={self.y}, z={self.z}, side={self.side})"

    def __str__(self) -> str:
        """User-friendly string representation.

        Returns:
            str: Human-readable description of the cube.
        """
        return f"Cube at ({self.x}, {self.y}, {self.z}) a={self.side}"
