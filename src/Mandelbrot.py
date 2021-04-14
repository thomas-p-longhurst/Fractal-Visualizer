from Fractal import Fractal


class Mandelbrot(Fractal):
    def __init__(self):
        """"""
        self.__MAX_ITERATIONS = 256

    def count(self, c):
        """Returns an int: given a complex coordinate, return the iteration count of the
        Mandelbrot function for that point. Can only be run in concrete subclasses.
        """
        z = complex(0.0, 0.0)

        for i in range(self.__MAX_ITERATIONS):
            z = z * z + c
            if abs(z) > 2:
                return i
        return self.__MAX_ITERATIONS
