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
    """Set up our PhotoImage, and establish the min and max x and y variables"""
```
#### `makeTkWindow()`
```python
def makeTkWindow():
    """Creates a TkWindow that we can paint on"""
```
#### `paint()`
```python
def paint():
    """Given a coordinate and a color, color the pixel accordingly"""
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

time_start = time()
painter = new ImagePainter
for i in range(0, painter.width):
    for j in range(0, painter.height):
        if we have a mandel fractal:
            iteration_count = mandelbrot.getIterationCount(i, j)
        elif we have a julia fractal:
            iteration_count = julia.getIterationCount(i, j)
        color = palette.getColor(iteration_count)
        painter.paint(i, j, color)
time_end = time()
print(f"Painting done in {time_end - time_start}")
painter.saveImage() 
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

```
#### `makeTkWindow()`
```pseudocode
img = PhotoImage(width=512, height=512)
window = Tk()
canvas = Canvas(window, width=512, height=512, bg='#ffffff')
canvas.pack()
canvas.create_image((256, 256), image=img, state="normal")
```

#### `paint()`
```pseudocode

```



# 3.  Function Template

**Combine the function stubs written in step #2 with pseudocode from step #3.
Comment out the pseudocode, leaving a valid program that compiles/runs without
errors.  At this stage your program doesn't quite work, but it also doesn't
crash.**


# 4.  Implementation

**This is the only part of the process focused on writing code in your chosen
programming language.**

**One by one translate passages of pseudocode into valid code.  Fill in the gaps
in the function template.  Exploit the purpose statement and the examples.**

**If you were thorough in the previous steps and are familiar with your
programming system this part will go by very quickly and the code will write
itself.**

**When you are learning a new programming language or an unfamiliar library this
phase can be slow and difficult.  As you gain experience with the relevant
technologies you will spend less and less time in this phase of the process.**


# 5.  Testing

**Articulate the examples given in step #2 as tests and ensure that each
function passes all of its tests.  Doing so discovers mistakes.  Tests also
supplement examples in that they help others read and understand the definition
when the need arises—and it will arise for any serious program.**

**As bugs are discovered and fixed, devise new test cases that will detect these
problems should they return.**

**If you didn't come across any bugs (lucky you!) think of a possible flaw and a
test that can be employed to screen for it.**

**At a minimum you should create a document explaining step-by-step how a
non-technical user may manually test your program to satisfy themselves that it
operates correctly.  Explain the entire process starting how to launch the
program, what inputs they should give and what results they should see at every
step.  Provide test cases of good and bad inputs to catch both false positives
and false negatives.  Any deviation from the expected outputs are errors.**

**The ideal is to write an automated test to avoid all manual labor beyond
launching the test.**
