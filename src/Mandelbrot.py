def getIterationCount(c, max_iterations):
    """Returns an int: given a complex coordinate and a max number of iterations, return
    the iteration count of the Mandelbrot function for that point
    """
    z = complex(0.0, 0.0)

    for i in range(max_iterations):
        z = z * z + c
        if abs(z) > 2:
            return i
    return max_iterations
