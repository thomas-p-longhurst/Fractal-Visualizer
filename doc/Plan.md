# 0.  From Problem Analysis to Data Definitions

This program draws a fractal in a new window. It goes pixel-by-pixel and determines the color of each pixel
through some formula that is above my paygrade.

# 1.  System Analysis

[main.py](../src/main.py) acts as the main entry point. This file should be a driver program, and
not much more.

[FractalInformation.py](../src/FractalInformation.py) defines a data structure that contains all fractal
configuration data

[Fractal.py](../src/Fractal.py) acts as an abstract parent class for `Mandelbrot.py`, `Julia.py`, and `Mandelbrot4.py`.

[Mandelbrot.py](../src/Mandelbrot.py), [Julia.py](../src/Julia.py), and [Mandelbrot4.py](../src/Mandelbrot4.py) are 
concrete classes that define specific formulas to get an "iteration count" from a single complex number.

[Palette.py](../src/Palette.py) is an abstract class that defines how to obtain a color from an iteration count. This 
will have three relatively trivial concrete classes: [PaletteBlackAndWhite.py](../src/PaletteBlackAndWhite.py), 
[PaletteDefault.py](../src/PaletteDefault.py), and [PaletteTrippy.py](../src/PaletteTrippy.py)

[ImagePainter.py](../src/ImagePainter.py) creates a `Tk` window and a `PhotoImage` object that respectively
display and save the fractal.

[FractalFactory.py](../src/FractalFactory.py) returns a concrete fractal object based upon a configuration file given
to it from the main program.

[PaletteFactory.py](../src/PaletteFactory.py) returns a concrete palette object specified by the user on the command 
line.

## Command Line Interface
Follows this format:
```
python src/main.py [FRACTAL_FILE [PALETTE_NAME]]
```

When no argument is supplied, all choices are presented to the user:
```
$ python main.py
FractalFactory: Creating default fractal
PaletteFactory: Creating default color palete

```

When one argument is given, it is used as the name of a fractal configuration file:
```
$ python src/main.py data/fulljulia.frac
PaletteFactory: Creating default color palette
```

When two arguments are given, the first is used as the name of a fractal configuration object and the second is
taken to be the name of a Palette:
```
$ python src/main.py data/funnel-down.frac ColorCube
```

When a configuration file is missing or inaccessible, the program exits with the error raised by `open()`
```
$ python src/main.py data/NOT_EXIST ColorCube
Traceback (most recent call last):
  File "src/main.py", line 26, in <module>
    fractal = FractalFactory.makeFractal(cfg)
  File "/home/fadein/cs1440-falor-erik-assn4/src/FractalFactory.py", line 30, in makeFractal
    cfg = __readFrac(cfgFile)
  File "/home/fadein/cs1440-falor-erik-assn4/src/FractalFactory.py", line 64, in __readFrac
    with open(cfgFile) as f:
FileNotFoundError: [Errno 2] No such file or directory: 'data/NOT_EXIST'
```

When an invalid palette name is given, the program exits with an error message
```
$ python src/main.py data/funnel-down.frac NOT_EXIST
Traceback (most recent call last):
  File "src/main.py", line 27, in <module>
    palette = PaletteFactory.makePalette(fractal.iterations, gtype=palette)
  File "/home/fadein/cs1440-falor-erik-assn4/src/PaletteFactory.py", line 49, in makePalette
    raise NotImplementedError("Invalid palette requested")
NotImplementedError: Invalid palette requested
```

## Fractal Configuration File Format
Examples can be found in [../data/](../data). In summary:
* Lines beginning with `#` are skipped
* Blank lines are skipped 
* Configuration parameters can appear in any order
* Names of configuration parameters are case-sensitive
* Parameter names are separated (delimited) from their values with a colon `:`
* White space is not significant; we can strip it away

These should be read into a dictionary.

When a configuration file is improperly filled out, the program must raise a `NotImplementedError` with a message:
```
raise NotImplementedError("Invalid fractal configuration file")
```

## Function Stubs
For brevity's sake, trivial getter methods and inherited methods have been omitted.
### `main.py`
#### `main()`
```python
if __name__ == '__main__':
    """Here be our main point of entry. Determine the desired fractal and palette, create them,
    and pass them on to ImagePainter.
    """
```

### `Fractal.py`
#### `getIterationCount()`
```python
def count():
    """Returns an int: given a complex coordinate, return the iteration count of the 
    Mandelbrot function for that point. Can only be run in concrete subclasses.
    """
```

### `Palette.py`
#### `getColor()`
```python
def getColor():
    """Returns a String: given an iteration count (int), return a string corresponding to a color. Can only be run
    in concrete subclasses."""
```

### `ImagePainter.py`
#### `__init__()`
```python
def __init__():
    """Set up our PhotoImage and everything else we need to draw our fractal"""
```
#### `paint()`
```python
def paint():
    """Paint a fractal to the screen"""
```
#### `saveImage()`
```python
def saveImage():
    """Given a file path, save the image to the disk"""
```

### `FractalFactory.py`
#### `makeFractal()`
```python
def makeFractal():
    """Returns a concrete palette object specified by a String."""
```

### `PaletteFactory.py`
#### `makePalette()`
```python
def makePalette():
    """Returns a concrete palette object specified by a String."""
```



# 2.  Functional Examples
### `main.py`
#### `main()`
```pseudocode
DEFAULT_FRACTAL = "mandelbrot"
DEFAULT_PALETTE = "default"

if len(sys.argv) < 2:
    print("FractalFactory: Creating default fractal")
    fractal = FractalFactory.makeFractal(DEFAULT_FRACTAL)
else:
    fractal = FractalFactory.makeFractal(sys.argv[2])
    
if len(sys.argv) < 3:    
    print("PaletteFactory: Creating default fractal")
    palette = PaletteFactory.makePalette(DEFAULT_PALETTE)
else:
    palette = PaletteFactory.makePalette(sys.argv[3])

painter = new ImagePainter()
painter.paint(fractal, palette)
```

### `Fractal.py`
#### `__init__()`
```pseudocode
raise NotImplementedError("Concrete subclass of Fractal must implement __init__")
```

#### `count()`
```pseudocode
raise NotImplementedError("Concrete subclass of Fractal must implement count() method")
```

### `Mandelbrot.py`
#### `count()`
```pseudocode
z = complex(0.0, 0.0)

for i in range(self.max_iterations):
    z = z * z + c
    if abs(z) > 2:
        return i
return self.max_iterations
```

### `Julia.py`
#### `count()`
```pseudocode
c = complex(-1.0, 0.0)

for i in range(self.max_iterations):
    z = z * z + c
    if abs(z) > 2:
        return i
return self.max_iterations
```

### `Mandelbrot4.py`
#### `count()`
```pseudocode
z = complex(0.0, 0.0)

for i in range(self.max_iterations):
    z = z ** 4 + c
    if abs(z) > 2:
        return i
return self.max_iterations
```

### `Palette.py`
#### `__init__()`
```pseudocode
raise NotImplementedError("Concrete subclass of Palette must implement __init__")
```

#### `getColor()`
```pseudocode
raise NotImplementedError("Concrete subclass of Palette must implement getColor()")
```

### `ImagePainter.py`
#### `__init__()`
```pseudocode
img = PhotoImage(width=512, height=512)
window = Tk()
canvas = Canvas(window, width=512, height=512, bg='#ffffff')
canvas.pack()
canvas.create_image((256, 256), image=img, state="normal")
```

#### `paint()`
```pseudocode
before = time.time()


# Figure out how the boundaries of the PhotoImage relate to coordinates on
# the imaginary plane.
minx = fractal.centerX - (fractal.axisLen / 2.0)
maxx = fractal.centerX + (fractal.axisLen / 2.0)
miny = fractal.centerY - (fractal.axisLen / 2.0)

# At this scale, how much length and height on the imaginary plane does one
# pixel take?
pixelsize = abs(maxx - minx) / 512    

for row in range(512, 0, -1):
    for col in range(512):
        x = minx + col * pixelsize
        y = miny + row * pixelsize
        
        iterationCount = fractal.count(complex(x, y))         
        
        color = palette.getColor(iterationCount)
        img.put(color, (col, 512 - row))
    window.update()  # display a row of pixels


# Save the image as a PNG
after = time.time()
print(f"Done in {after - before:.3f} seconds!", file=sys.stderr)
saveImage()
```

#### `saveImage()`
```pseudocode
img.write(f"{fractal}.png")
print(f"Wrote image {fractal}.png")

# Call tkinter.mainloop so the GUI remains open
print("Close the image window to exit the program")
mainloop()
```

### `FractalFactory.py`
#### `makeFractal()`
```
fractal_config = open(fractal_file)
info = new dictionary()
for line in fractal_config:
    if line[0] == '#' or if the line is blank:
        continue
    strip the line
    items = line.split(":")
    if items[0] in int_fields:
        items[1] = int(items[1])
    info[items[0]] = items[1]
fractal_config.close()

for field in required_fields:
    if field not in info.keys():
        raise NotImplementedError(f"Field {field} is missing from configuration file.")
    
type = info["type"]
if type == "mandelbrot":
    fractal = new Mandelbrot(info)
elif type == "julia" or type == "burningshipjulia":
    fractal = new Julia(info)
else:
    raise NotImplementedError("Invalid fractal type")

return fractal
```

### `PaletteFactory.py`
#### `makePalette()`
```
if palette_name == "default":
    palette = new PaletteDefault()
elif palette_name == "black_and_white":
    palette = new PaletteBlackAndWhite()
elif palette_name == "trippy":
    palette = new PaletteTrippy()
else:
    raise NotImplementedError("Invalid palette requested")
```


# 3.  Function Template

### `main.py`
#### `main()`
```python
if __name__ == '__main__':
    """Here be our main point of entry. Determine the desired fractal and palette, create them,
    and pass them on to ImagePainter.
    """
    # DEFAULT_FRACTAL = "mandelbrot"
    # DEFAULT_PALETTE = "default"
    # 
    # if len(sys.argv) < 2:
    #     print("FractalFactory: Creating default fractal")
    #     fractal = FractalFactory.makeFractal(DEFAULT_FRACTAL)
    # else:
    #     fractal = FractalFactory.makeFractal(sys.argv[2])
    #     
    # if len(sys.argv) < 3:    
    #     print("PaletteFactory: Creating default fractal")
    #     palette = PaletteFactory.makePalette(DEFAULT_PALETTE)
    # else:
    #     palette = PaletteFactory.makePalette(sys.argv[3])
    # 
    # painter = new ImagePainter()
    # painter.paint(fractal, palette)
    pass
```

### `Mandelbrot.py`
#### `count()`
```python
def count():
    """Returns an int: given a complex coordinate, return the iteration count of the 
    Mandelbrot function for that point. Can only be run in concrete subclasses.
    """
    # z = complex(0.0, 0.0)
    # 
    # for i in range(self.MAX_ITERATIONS):
    #     z = z * z + c
    #     if abs(z) > 2:
    #         return i
    # return self.MAX_ITERATIONS
    return 0
```

### `Julia.py`
#### `count()`
```python
def count():
    """Returns an int: given a complex coordinate, return the iteration count of the 
    Mandelbrot function for that point. Can only be run in concrete subclasses.
    """
    # c = complex(-1.0, 0.0)
    # 
    # for i in range(self.__MAX_ITERATIONS):
    #     z = z * z + c
    #     if abs(z) > 2:
    #         return i
    # return self.__MAX_ITERATIONS
    return 0
```

### `Mandelbrot4.py`
#### `count()`
```python
def count():
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
```
### `Palette.py`
#### `getColor()`
```python
def getColor():
    """Returns a String: given an iteration count (int), return a string corresponding to a color. Can only be run
    in concrete subclasses."""
    # raise NotImplementedError("Concrete subclass of Palette must implement getColor()")
    return '#000000'
```

### `ImagePainter.py`
#### `__init__()`
```python
def __init__():
    """Set up our PhotoImage and everything else we need to draw our fractal"""
    # img = PhotoImage(width=512, height=512)
    # window = Tk()
    # canvas = Canvas(window, width=512, height=512, bg='#ffffff')
    # canvas.pack()
    # canvas.create_image((256, 256), image=img, state="normal")
    pass
```
#### `paint()`
```python
def paint():
    """Paint a fractal to the screen"""
    # before = time.time()
    # 
    # 
    # # Figure out how the boundaries of the PhotoImage relate to coordinates on
    # # the imaginary plane.
    # minx = fractal.centerX - (fractal.axisLen / 2.0)
    # maxx = fractal.centerX + (fractal.axisLen / 2.0)
    # miny = fractal.centerY - (fractal.axisLen / 2.0)
    # 
    # # At this scale, how much length and height on the imaginary plane does one
    # # pixel take?
    # pixelsize = abs(maxx - minx) / 512    
    # 
    # for row in range(512, 0, -1):
    #     for col in range(512):
    #         x = minx + col * pixelsize
    #         y = miny + row * pixelsize
    #         
    #         iterationCount = fractal.count(complex(x, y))         
    #         
    #         color = palette.getColor(iterationCount)
    #         img.put(color, (col, 512 - row))
    #     window.update()  # display a row of pixels
    # 
    # 
    # # Save the image as a PNG
    # after = time.time()
    # print(f"Done in {after - before:.3f} seconds!", file=sys.stderr)
```
#### `saveImage()`
```python
def saveImage():
    """Given a file path, save the image to the disk"""
    # img.write(f"{fractal}.png")
    # print(f"Wrote image {fractal}.png")
    # 
    # # Call tkinter.mainloop so the GUI remains open
    # print("Close the image window to exit the program")
    # mainloop()
```

### `FractalFactory.py`
```python
def makeFractal():
    """Returns a concrete palette object specified by a String."""
    # fractal_config = open(fractal_file)
    # info = new dictionary()
    # for line in fractal_config:
    #     if line[0] == '#' or if the line is blank:
    #         continue
    #     strip the line
    #     items = line.split(":")
    #     if items[0] in int_fields:
    #         items[1] = int(items[1])
    #     info[items[0]] = items[1]
    # fractal_config.close()
    # 
    # for field in required_fields:
    #     if field not in info.keys():
    #         raise NotImplementedError(f"Field {field} is missing from configuration file.")
    #     
    # type = info["type"]
    # if type == "mandelbrot":
    #     fractal = new Mandelbrot(info)
    # elif type == "julia" or type == "burningshipjulia":
    #     fractal = new Julia(info)
    # else:
    #     raise NotImplementedError("Invalid fractal type")
    # 
    # return fractal
    return None
```

### `PaletteFactory.py`
```python
def makePalette():
    """Returns a concrete palette object specified by a String."""
    # if palette_name == "default":
    #     palette = new PaletteDefault()
    # elif palette_name == "black_and_white":
    #     palette = new PaletteBlackAndWhite()
    # elif palette_name == "trippy":
    #     palette = new PaletteTrippy()
    # else:
    #     raise NotImplementedError("Invalid palette requested")
    return None
```


# 4.  Implementation

See [src](../src)

# 5.  Testing

See [unit test](../src/Testing). In addition to unit tests, I have images produced by commit 
`7a33a7d77ce23acdd00045ce624d8246210328a8`, and I will use `diff` to see if the images the new program produces are
exactly the same.