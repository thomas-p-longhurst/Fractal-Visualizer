from Fractal import Fractal


class Mandelbrot4(Fractal):
    def __init__(self):
        pass

    def count(self, c):
        """Returns an int: given a complex coordinate, return the iteration count of the
        Mandelbrot function for that point. Can only be run in concrete subclasses.
        """
        # z = complex(0.0, 0.0)
        #
        # for i in range(max_iterations):
        #     z = z ** 4 + c
        #     if abs(z) > 2:
        #         return i
        # return max_iterations
        return 0
