import Mandelbrot, Mandelbrot4, Julia
import FractalInformation


def makeFractal(fractal_info):
    """Returns a concrete palette object specified by a String."""

    type = fractal_info["type"]
    if type == "mandelbrot":
        # fractal = new Mandelbrot(info)
        fractal = Mandelbrot.Mandelbrot(fractal_info)
    elif type == "julia" :
        # fractal = new Julia(info)
        fractal = Julia.Julia(fractal_info)
    elif type == "mandelbrot4":
        fractal = Mandelbrot4.Mandelbrot4(fractal_info)
    else:
        raise NotImplementedError(f"Fractal type \"{type}\" is either invalid or has not been implemented")

    return fractal
