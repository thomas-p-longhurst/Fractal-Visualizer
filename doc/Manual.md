# Fractal Visualizer User Manual

## 1. Usage
```
$ py main.py [FRACTAL_FILE [PALETTE_NAME]]
```

0. FRACTAL_FILE is the name of a fractal configuration file in [../data](../data). 
1. PALETTE_NAME is the name of a palette. Currently, there are three palettes:
    * `default`
    * `black_and_white`
    * `trippy`

If neither argument is provided, the program will default to the full mandelbrot set and the palette `default`.
If only `PALETTE_NAME` is missing, the program will default to the palette `default`. The program cannot
be run with only `PALETTE_NAME`.

## 2. Saving an Image
All generated images are automatically saved to the directory from which `main.py` was run. The name of the
image will be the fractal pattern followed by `.png`, i.e. running the program with the argument `spiral0`
will generate the image `spiral0.png`. 

Note: This will overwrite any other files with the exact same name. Unless you collect .png files of 
fractals, this shouldn't be an issue.

## 3. Creating Custom Fractals
Custom fractals can be made by creating a `.frac` file in any text editor. Each line in these files is a field 
consisting of a key and value separated by a colon `:`. For Mandelbrot sets, there are six required fields:

| Field      | Data type | Description |
|------------|-----------|-------------|
| type       | String    | Describes which fractal formula to apply, i.e. `mandelbrot`, `mandelbrot4`, `julia`
| centerx    | float     | The center point of the image along the X axis
| centery    | float     | The center point of the image along the Y axis
| axislength | float     | The distance that this image covers. A larger image will be zoomed out, and a smaller value will be zoomed in.
| pixels     | int       | The width (and height) of the image in pixels.
| iterations | int       | How many iterations the program will loop before giving up on a pixel.

For Julia sets, you must also specify the following fields:

| Field | Data type | Description |
|-------|-----------|-------------|
| creal | float     | The real component of the constant `C` used by the Julia formula
| cimag | float     | The imaginary component of the constant `C` used by the Julia formula

These fields are not case-sensitive. Blank lines will be ignored, and lines starting with `#` will be treated as a comment.
If any of the required fields are missing, the program will raise an error.