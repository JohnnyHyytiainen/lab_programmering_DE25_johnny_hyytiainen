# Kommentarer: Svenska
# Kod: Engelska


class Circle:
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius

    def area(self):
        return 3.14 * self.radius**2

    def translate(self, dx, dy):
        self.x += dx
        self.y += dy


c = Circle(0, 0, 5)
print(c.area())
c.translate(2, 3)
print(c.x, c.y)
