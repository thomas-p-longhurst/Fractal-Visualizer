import Mandelbrot, Mandelbrot4, Julia

REQUIRED_FIELDS = ["type", "centerx", "centery", "axislength", "pixels", "iterations"]
REQUIRED_JULIA_FIELDS = ["creal", "cimag"]
INT_FIELDS = ["pixels", "iterations"]
FLOAT_FIELDS = ["centerx", "centery", "axislength", "creal", "cimag"]


def makeFractal(fractal_file):
    """Returns a concrete palette object specified by a String."""
    fractal_config = open(fractal_file)
    # info = new dictionary()
    info = {}
    for line in fractal_config:
        line = line.strip().lower()
        # if line[0] == '#' or if the line is blank:
        if not bool(line):
            continue
        if line[0] == '#':
            continue

        items = line.split(": ")
        key = items[0]
        value = items[1]

        if len(items) < 2:
            raise NotImplementedError(f"Key \"{key}\" has no value")

        if key in FLOAT_FIELDS:
            try:
                value = float(value)
            except ValueError:
                raise NotImplementedError(f"Key \"{key}\" must have a float value (was \"{value}\")")
        if key in INT_FIELDS:
            if not value.isnumeric():
                raise NotImplementedError(f"Key \"{key}\" must have an int value (was \"{value}\")")
            value = int(value)

        info[key] = value
    fractal_config.close()

    for field in REQUIRED_FIELDS:
        if field not in info.keys():
            raise NotImplementedError(f"Field {field} is missing from configuration file.")

    type = info["type"]
    if type == "mandelbrot":
        # fractal = new Mandelbrot(info)
        fractal = Mandelbrot.Mandelbrot(info)
    elif type == "julia" or type == "burningshipjulia":
        # fractal = new Julia(info)
        for field in REQUIRED_JULIA_FIELDS:
            if field not in info.keys():
                raise NotImplementedError(f"Field {field} is missing from configuration file.")
        fractal = Julia.Julia(info)
    elif type == "mandelbrot4":
        fractal = Mandelbrot4.Mandelbrot4(info)
    else:
        raise NotImplementedError(f"Invalid fractal type \"{type}\"")

    return fractal
