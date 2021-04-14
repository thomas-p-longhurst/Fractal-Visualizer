from abc import ABC


class Fractal(ABC):
    def __init__(self):
        raise NotImplementedError("Concrete subclass of Fractal must implement __init__")

    def count(self, coord):
        """Returns an int: given a complex coordinate, return the iteration count of the
        Mandelbrot function for that point. Can only be run in concrete subclasses.
        """
        raise NotImplementedError("Concrete subclass of Fractal must implement count() method")