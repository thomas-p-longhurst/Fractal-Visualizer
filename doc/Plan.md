# 0.  From Problem Analysis to Data Definitions

This program draws a fractal in a new window. It goes pixel-by-pixel and determines the color of each pixel
through some formula that is above my paygrade.

# 1.  System Analysis

[main.py](../src/main.py) acts as the main entry point. This file should be a driver program, and
not much more.

[FractalInformation.py](../src/FractalInformation.py) defines a data structure that contains all fractal
configuration data

[Mandelbrot.py](../src/Mandelbrot.py) and [Julia.py](../src/Julia.py) are used to get the "iteration count"
(tl;dr: fancy math stuff to make fractal images) for their respective fractal algorithms.

[Palette.py](../src/Palette.py) is used to determine the color of a pixel given an iteration count.

[ImagePainter.py](../src/ImagePainter.py) creates a `Tk` window and a `PhotoImage` object that respectively
display and save the fractal.

## Command Line Interface
When no argument is supplied, all choices are presented to the user:
```
$ python main.py
Please provide the name of a fractal as an argument
    fulljulia
    hourglass
    lakes
    mandelbrot
    spiral0
    spiral1
    seahorse
    elephants
    leaf

```

An invalid argument is reported as an error and is followed by the usage message:
```
$ python main.py moustache
ERROR: moustache is not a valid fractal
Please choose one of the following:
    mandelbrot
    spiral0
    spiral1
    seahorse
    elephants
    leaf
    fulljulia
    hourglass
    lakes

```

## Function Stubs
For brevity's sake, trivial getter methods have been omitted.
### `main.py`
#### `main()`
```python
if __name__ == '__main__':
    """Here be our main point of entry. At the end of the day, we'll have to determine 
    the user's desired fractal, and pass that information on to ImagePainter.py
    """
```

### `Mandelbrot.py`
#### `getIterationCount()`
```python
def getIterationCount():
    """Returns an int: given a complex coordinate and a max number of iterations, return 
    the iteration count of the Mandelbrot function for that point
    """
```

### `Julia.py`
#### `getIterationCount()`
```python
def getIterationCount():
    """Returns an int: given a complex coordinate and a max number of iterations, return 
    the iteration count of the Mandelbrot function for that point
    """
```

### `Palette.py`
#### `getColor()`
```python
def getColor():
    """Returns a String: given an iteration count, return a string corresponding to a color"""
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



# 2.  Functional Examples
### `main.py`
#### `main()`
```pseudocode
if len(sys.argv) < 2:
    print("Please provide the name of a fractal as an argument")
    for pattern in FractalInformation.dictionary:
        print pattern.name
desired_fractal = sys.argv[2]
if desired_fractal is not in FractalInformation.dictionary:
    print(f"ERROR: {desired_fractal} is not a valid fractal)
    print("Please choose one of the following:")
    for pattern in FractalInformation.dictionary:
        print pattern.name

fractal = FractalInformation.dictionary[desired_fractal]

painter = new ImagePainter()
painter.paint(fractal)
```

### `Mandelbrot.py`
#### `getIterationCount()`
```pseudocode
z = complex(0.0, 0.0)

for i in range(max_iterations):
    z = z * z + c
    if abs(z) > 2:
        return i
return max_iterations
```

### `Julia.py`
#### `getIterationCount()`
```pseudocode
c = complex(-1.0, 0.0)

for i in range(max_iterations):
    z = z * z + c
    if abs(z) > 2:
        return i
return max_iterations
```

### `Palette.py`
#### `getColor()`
```pseudocode
if iterationCount >= len(colors):
    return colors[-1]
return colors[iterationCount]
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
minx = fractal['centerX'] - (fractal['axisLen'] / 2.0)
maxx = fractal['centerX'] + (fractal['axisLen'] / 2.0)
miny = fractal['centerY'] - (fractal['axisLen'] / 2.0)

# At this scale, how much length and height on the imaginary plane does one
# pixel take?
pixelsize = abs(maxx - minx) / 512    

for row in range(512, 0, -1):
    for col in range(512):
        x = minx + col * pixelsize
        y = miny + row * pixelsize
        
        if fractal['type'] == "Mandelbrot":
            iterationCount = Mandelbrot.getIterationCount(complex(x, y))
        elif fractal['type'] == "Julia":
            iterationCount = Julia.getIterationCount(complex(x, y))            
        
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



# 3.  Function Template

### `main.py`
#### `main()`
```python
if __name__ == '__main__':
    """Here be our main point of entry. At the end of the day, we'll have to determine 
    the user's desired fractal, and pass that information on to ImagePainter.py
    """
    # if len(sys.argv) < 2:
    #     print("Please provide the name of a fractal as an argument")
    #     for pattern in FractalInformation.dictionary:
    #         print pattern.name
    # desired_fractal = sys.argv[2]
    # if desired_fractal is not in FractalInformation.dictionary:
    #     print(f"ERROR: {desired_fractal} is not a valid fractal)
    #     print("Please choose one of the following:")
    #     for pattern in FractalInformation.dictionary:
    #         print pattern.name
    # 
    # fractal = FractalInformation.dictionary[desired_fractal]
    # 
    # painter = new ImagePainter()
    # painter.paint(fractal)
    pass
```

### `Mandelbrot.py`
#### `getIterationCount()`
```python
def getIterationCount():
    """Returns an int: given a complex coordinate and a max number of iterations, return 
    the iteration count of the Mandelbrot function for that point
    """
    # z = complex(0.0, 0.0)
    # 
    # for i in range(max_iterations):
    #     z = z * z + c
    #     if abs(z) > 2:
    #         return i
    # return max_iterations
    return 0
```

### `Julia.py`
#### `getIterationCount()`
```python
def getIterationCount():
    """Returns an int: given a complex coordinate and a max number of iterations, return 
    the iteration count of the Mandelbrot function for that point
    """
    # c = complex(-1.0, 0.0)
    # 
    # for i in range(max_iterations):
    #     z = z * z + c
    #     if abs(z) > 2:
    #         return i
    # return max_iterations
    return 0
```

### `Palette.py`
#### `getColor()`
```python
def getColor():
    """Returns a String: given an iteration count, return a string corresponding to a color"""
    # if iterationCount >= len(colors):
    #     return colors[-1]
    # return colors[iterationCount]
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
    # minx = fractal['centerX'] - (fractal['axisLen'] / 2.0)
    # maxx = fractal['centerX'] + (fractal['axisLen'] / 2.0)
    # miny = fractal['centerY'] - (fractal['axisLen'] / 2.0)
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
    #         if fractal['type'] == "Mandelbrot":
    #             iterationCount = Mandelbrot.getIterationCount(complex(x, y))
    #         elif fractal['type'] == "Julia":
    #             iterationCount = Julia.getIterationCount(complex(x, y))            
    #         
    #         color = palette.getColor(iterationCount)
    #         img.put(color, (col, 512 - row))
    #     window.update()  # display a row of pixels
    # 
    # 
    # # Save the image as a PNG
    # after = time.time()
    # print(f"Done in {after - before:.3f} seconds!", file=sys.stderr)
    # saveImage(img)
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


# 4.  Implementation

See [src](../src)

# 5.  Testing

See [unit test](../src/Testing). In addition to unit tests, I have images produced by commit 
`7a33a7d77ce23acdd00045ce624d8246210328a8`, and I will use `diff` to see if the images the new program produces are
exactly the same.