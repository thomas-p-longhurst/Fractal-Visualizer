# Fractal Visualizer User Manual

## 1. Usage
```
$ py main.py <Fractal-Pattern>
```
Below is a table showing the supported fractal patterns

| Description    | <Fractal-Pattern>   |
|----------------|---------------------|
| Mandelbrot Set | `mandelbrot`        |
| Spiral 0       | `spiral0`           |
| Spiral 1       | `spiral1`           |
| Seahorse       | `seahorse`          |
| Elephants      | `elephants`         |
| Leaf           | `leaf`              |
| Julia Set      | `fulljulia`         |
| Hourglass      | `hourglass`         |
| Lakes          | `lakes`             |

## 2. Saving an Image
All generated images are automatically saved to the directory from which `main.py` was run. The name of the
image will be the fractal pattern followed by `.png`, i.e. running the program with the argument `spiral0`
will generate the image `spiral0.png`. 

Note: This will overwrite any other files with the exact same name. Unless you collect .png files of 
fractals, this shouldn't be an issue.

## 3. Adding Custom Patterns
Currently, custom patterns aren't supported. The only way to currently do this is to modify the source 
code. This feature is Coming Soon™
