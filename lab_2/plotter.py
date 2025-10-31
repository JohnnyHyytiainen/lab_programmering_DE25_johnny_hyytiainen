# Kommentarer: Svenska
# Kod: Engelska
# plotter.py
from pathlib import Path
import os
import matplotlib.pyplot as plt
from matplotlib.patches import Circle as PCircle, Rectangle as PRect
from circle import Circle
from rectangle import Rectangle


def _ensure_png(path) -> str:
    # Gör Path/str robust
    path = str(path)
    root, ext = os.path.splitext(path)
    return path if ext.lower() == ".png" else path + ".png"


class Shape2dPlotter:
    """Plot multiple 2D shapes (Circle, Rectangle) into the same axes."""

    def __init__(self, fig=None, ax=None):
        if fig is None or ax is None:
            fig, ax = plt.subplots(figsize=(6, 4))
        self.fig, self.ax = fig, ax
        # bounds som växer jag ritar
        self.minx = self.miny = float("inf")
        self.maxx = self.maxy = float("-inf")

    def _update_bounds(self, x0, y0, x1, y1):
        self.minx = min(self.minx, x0)
        self.miny = min(self.miny, y0)
        self.maxx = max(self.maxx, x1)
        self.maxy = max(self.maxy, y1)

    def draw(self, shape):
        """Draw ONE shape and update bounds.
        With center dot + label outside.
        """
        if isinstance(shape, Circle):
            # patch + centerpunkt(röd)
            self.ax.add_patch(PCircle((shape.x, shape.y), shape.radius, fill=False))
            self.ax.plot(shape.x, shape.y, "ro", markersize=3.5)
            x0, y0 = shape.x - shape.radius, shape.y - shape.radius
            x1, y1 = shape.x + shape.radius, shape.y + shape.radius
            self._update_bounds(x0, y0, x1, y1)
            return

        if isinstance(shape, Rectangle):
            # hörn från center
            x0 = shape.x - shape.width / 2
            y0 = shape.y - shape.height / 2
            x1 = x0 + shape.width
            y1 = y0 + shape.height
            # patch + centerpunkt (blå)
            self.ax.add_patch(PRect((x0, y0), shape.width, shape.height, fill=False))
            self.ax.plot(shape.x, shape.y, "bo", markersize=3.5)
            self._update_bounds(x0, y0, x1, y1)
            return
        # Hjälp om typerna inte matchar modulen
        raise TypeError(
            f"Stödjer ej {type(shape)}. " "import Circle/Rectangle från samma modul."
        )

    def draw_many_and_save(self, shapes, filename=None):
        """Draw many, autoscale + save. Return filepath."""
        if not shapes:
            raise ValueError("Shapes får ej vara tomma")

        for s in shapes:
            self.draw(s)

        # autoscale
        pad = 0.1 * max(self.maxx - self.minx, self.maxy - self.miny)
        self.ax.set_xlim(self.minx - pad, self.maxx + pad)
        self.ax.set_ylim(self.miny - pad, self.maxy + pad)
        self.ax.set_aspect("equal", adjustable="box")
        self.ax.set_xlabel("x")
        self.ax.set_ylabel("y")
        self.ax.set_title("2D Shapes")
        # "styling" dashed rutnät + top+left spine borta
        self.ax.grid(True, linestyle="--", alpha=0.5)
        self.ax.spines[["top", "right"]].set_visible(False)

        # filnamn: alltid lab_2/plots/lab_2_plot.png om inget anges
        if filename is None:
            filename = Path(__file__).resolve().parent / "plots" / "lab_2_plot.png"
        filename = _ensure_png(filename)

        # skapa mapp och spara
        outdir = os.path.dirname(filename) or "."
        os.makedirs(outdir, exist_ok=True)
        self.fig.tight_layout()
        abs_path = os.path.abspath(filename)
        self.fig.savefig(abs_path, dpi=150)
        plt.close(self.fig)
        return abs_path


def plot_shapes(shapes, filename=None):
    return Shape2dPlotter().draw_many_and_save(shapes, filename)


if __name__ == "__main__":
    shapes = [
        Circle(0, 0, 1),
        Rectangle(2.5, 0, 2, 1),
        Circle(-2, 1, 0.5),
    ]
    out = plot_shapes(shapes)
    print("Plot sparad som lab_2_plot.png och finns i din:\n", out, "folder")
