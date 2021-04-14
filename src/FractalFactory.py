import Mandelbrot, Mandelbrot4, Julia
import FractalInformation


def makeFractal(fractal_file):
    """Returns a concrete palette object specified by a String."""
    info = FractalInformation.makeFractalInfo(fractal_file)

    type = info["type"]
    if type == "mandelbrot":
        # fractal = new Mandelbrot(info)
        fractal = Mandelbrot.Mandelbrot(info)
    elif type == "julia" :
        # fractal = new Julia(info)
        fractal = Julia.Julia(info)
    elif type == "mandelbrot4":
        fractal = Mandelbrot4.Mandelbrot4(info)
    else:
        raise NotImplementedError(f"Fractal type \"{type}\" is either invalid or has not been implemented")

    return fractal
