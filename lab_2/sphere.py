# Kommentarer: Svenska
# Kod: Engelska
# sphere.py


# Decorator. Functools för att slippa upprepa mig själv med operator overloads.
# @total_ordering gör att jag enbart behöver skriva __eq__ + __lt__ (Lika med + mindre än)
# Följer DRY konceptet extra mycket tack vare denna decorator, likadant som med cube.py
from functools import total_ordering

# importera 3D basklass
from shape3d import Shape3D
import math


@total_ordering
class Sphere(Shape3D):
    """
    Sphere defined by a center point(x,y,z) and a radius.
    Inherits (x, y, z) and translate() from Shape3D parent.
    """

    def __init__(
        self, x: float | int, y: float | int, z: float | int, radius: float | int
    ):
        """Initializes the sphere.

        Args:
            x, y, z (float | int): Center coordinates.
            radius (float | int): Radius (must be > 0).

        Raises:
            TypeError: If any argument is not numeric.
            ValueError: If radius <= 0.
        """
        # skicka x,y,z till parent class(Shape3D)
        super().__init__(x, y, z)
        # hanterar enbart det som är unikt för Sphere klassen
        if not isinstance(radius, (int, float)):
            raise TypeError("radius must be a number!")
        if radius <= 0:
            raise ValueError("radius must be > 0")
        self.radius = float(radius)

    # @property decorator istället för att använda mig utav getter funktion för Shape3D
    # @property gör mina värden read-only
    # Följa DRY konceptet
    @property
    def surface_area(self) -> float:
        """Surface area of the sphere (4 * pi * r^2)"""
        return 4.0 * math.pi * self.radius**2

    # Samma @property kommentar som ovan.
    @property
    def volume(self) -> float:
        """Volume of the sphere ((4/3) * pi * r^3)"""
        return (4.0 / 3.0) * math.pi * self.radius**3

    # Ärver translate ifrån parent class Shape3D
    # Behöver EJ skriva det här -> DRY

    def is_unit_sphere(self) -> bool:
        """Checks if the sphere is a unit sphere.

        Returns:
          bool: True if radius is approximately 1.0.
        """
        return math.isclose(self.radius, 1.0)
        # .isclose går att använda tack vare import math. .isclose passar perfekt att använda om jag jobbar med floats.

    # Två operators behövs för att total_ordering decoratorn ska bli användbar == DRY
    # (__eq__ + __lt__ behövs för detta. Lika med + mindre än)
    def __eq__(self, other: object) -> bool:
        """Two spheres are equal if they got the same radius"""
        if not isinstance(other, Sphere):
            return False
        return math.isclose(self.radius, other.radius)
        # .isclose går att använda tack vare import math. .isclose passar perfekt att använda om jag jobbar med floats.

    # operator nr 2 som behövs total_ordering. DRY

    def __lt__(self, other: object) -> bool:
        if hasattr(other, "volume"):
            # hasattr = inbyggd funktion för att kolla om objekt har en specifik attribut/metod och ger True om dom finns annars False.
            # Använder det för att förhindra AttributeError.
            return self.volume < other.volume
        return NotImplemented

    def __repr__(self) -> str:
        """Developer-friendly representation (recreatable)."""
        return f"Sphere(x={self.x}, y={self.y}, z={self.z}, radius={self.radius})"

    def __str__(self) -> str:
        """User-friendly string representation.

        Returns:
            str: Human-readable description of the sphere.
        """
        return f"Sphere is at ({self.x}, {self.y}, {self.z}) r={self.radius}"
