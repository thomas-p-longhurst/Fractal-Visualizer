from abc import ABC


class Palette(ABC):
    def __init__(self):
        raise NotImplementedError("Concrete subclass of Palette must implement __init__")

    def getColor(self, iterationCount):
        """Returns a String: given an iteration count (int), return a string corresponding to a color. Can only be run
        in concrete subclasses."""
        raise NotImplementedError("Concrete subclass of Palette must implement getColor()")

