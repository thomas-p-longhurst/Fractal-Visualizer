# CS 1440 Assignment 4.1 Instructions

## Description

Take this fractal generating program to the next level by applying good
principles of *Object-Oriented Design*.  Your goal is to create a program that
can stand the test of time by being easy to test, modify and extend.

Additionally, because your program accepts input files in a standard format,
you will be able to share your fractal creations with your classmates.


## Previous Semester Assignment Statistics

Statistic                        | Value
--------------------------------:|:---------------
Average Hours Spent              | 13.2
Average Score % (Grade)          | 75.38% (C)
% students thought this was Easy |  6.25%
... Medium                       | 55.47%
... Hard                         | 32.81%
... Too Hard/Did not complete    |  5.47%


## Overview

After successfully refactoring your client's program into a form which is
easier to work on and think about, you are ready to take this program to the
next level.  In this sprint you will apply the [Factory
Method](https://sourcemaking.com/design_patterns/factory_method) design pattern
to your code.  Through judicious use of this design pattern your program will
evolve from being merely maintainable to easily extensible.  A little bit of
planning and energy spent now will set the stage for many years of smooth
maintenance in the future.


## Objectives

-   Re-organize modules into Polymorphic (duck typed) classes
    -   Take advantage of code reuse through *inheritance*
-   Use the *Factory Method* design pattern to easily create new fractal & palette objects at runtime
-   Employ the *Strategy* design pattern to make a program can pick an appropriate algorithm from user input
    -   Implement hard-coded default behaviors which may be overridden by user
-   Update the documentation (UML, manual, etc.) from the previous assignment so that it remains congruent with final product
-   Perform detailed integration testing to prove that your design is robust


## Submission Instructions

Upon completion of Assignment 4.1 push your code to GitLab as usual.



## Requirements

0.  Define a `Fractal` abstract class and *three* concrete sub-classes
    -   The `Fractal` abstract class exists solely to provide a common
        structure to the concrete classes that inherit from it.  Your program
        will not create plain `Fractal` objects.  It will instead use classes
        derived from `Fractal` through inheritance.
    -   The `Fractal` class cannot be instantiated because its `__init__`
        method is a placeholder which raises [`NotImplementedError`](https://docs.python.org/3/library/exceptions.html#NotImplementedError)
        when called.  It need only consist of this line of code:
        `raise NotImplementedError("Concrete subclass of Fractal must implement __init__")`
    -   `Fractal` provides a placeholder `count()` method which raises an
        exception when called.  It consists solely of this statement:
        `raise NotImplementedError("Concrete subclass of Fractal must implement count() method")`
    -   You are allowed (but not required) to write other methods besides
        `count()`.  These methods do not need to raise `NotImplementedError`.
        These methods would then be available in all derived classes of
        `Fractal`.
    -   The `Julia` and `Mandelbrot` classes inherit their structure from the
        abstract class `Fractal`, and are obligated to provide their own
        implementations of `__init__` and `count()` such that they will not
        raise `NotImplementedError` when used.
    -   `count()` takes one complex number as input and returns an integer
        that is the number of iterations tried before the absolute value of the
        Fractal formula grew larger than `2.0`; otherwise the maximum number of
        iterations is returned.  This operation is the defining characteristic
        of a `Fractal` object.
    -   Other data used by `count()` are supplied through `self`, if needed.
    -   Define at least **one** new concrete subclass of `Fractal` following the
        pattern set forth by `Julia` and `Mandelbrot` but using different
        formulae.  You may choose from
        *   [Mandelbrot3 and Mandelbrot4](http://usefuljs.net/fractals/docs/multibrot.html)
        *   [Phoenix, BurningShip, and BurningShipJulia](http://usefuljs.net/fractals/docs/mandelvariants.html).
        You may also devise your own fractal formula.  Get creative!  If your
        new fractal class requires new configuration parameters, augment your
        `FractalFactory` class to handle then.
    -   The concrete sub-classes of `Fractal` are used _interchangeably_ in
        your program.  This is an example of polymorphism in action: objects of
        different classes which are used in the same way.  The code which uses
        a `Fractal`-derived object does not inspect the object to determine
        what kind of fractal it is; it just works because it defines the
        `count()` method.
    -   `Fractal` objects have no relation whatsoever to `Palettes` nor any
        knowledge about `Colors`.
1.  `FractalFactory` class or module
    -   Follow the [Factory Method Pattern](https://sourcemaking.com/design_patterns/factory_method)
        in your program when you need to instantiate objects embodying fractal
        algorithms.  `FractalFactory` returns a concrete fractal object based
        upon a configuration file given to it from the main program.  See below
        for details about the format of the fractal configuration file.
    -   The file defining `FractalFactory` is the only place in your entire
        program where your concrete `Fractal`-derived classes need to be
        imported.
    -   The `FractalFactory` itself doesn't have to be an object that you
        instantiate; it can be a function within a module.

        For example, this is how a `FractalFactory` object would be used:

        ```
        from FractalFactory import FractalFactory

        factory = FractalFactory()
        fractal = factory.makeFractal(sys.argv[1])
        ```

        Instead, `FractalFactory` might be a module containing the function `makeFractal()`:

        ```
        import FractalFactory

        fractal = FractalFactory.makeFractal(sys.argv[1])
        ```
    -   When no fractal configuration file is specified by the user on the
        command line, `FractalFactory` produces a "default" fractal
        configuration dictionary that is hard-coded into your program.
        -   Note: hard-coding the *path* to a fractal configuration file in
            `data/` is **not acceptable**.  Include the literal configuration
            dictionary for that fractal directly in your code.
    -   `FractalFactory` must perform some error checking upon the contents of
        the fractal configuration file it uses to create a `Fractal` object.
        *   When a missing or inaccessible fractal is called for, simply let the `open()` function fail.
        *   When an unrecognized fractal type is encountered, raise [`NotImplementedError`](https://docs.python.org/3/library/exceptions.html#NotImplementedError)
        *   When a fractal configuration file contains other errors, raise [`RuntimeError`](https://docs.python.org/3/library/exceptions.html#RuntimeError).  Possible errors are described in the section "Fractal Configuration File Format" below.
2.  Create a `Palette` abstract class and *two* concrete sub-classes
    -   The `Palette` abstract class exists solely to provide a common
        structure to the concrete classes that inherit from it.  Your program
        will not create plain `Palette` objects.  It will instead use classes
        derived from `Palette` through inheritance.
    -   The `Palette` class cannot be instantiated because its `__init__`
        method is a placeholder which raises [`NotImplementedError`](https://docs.python.org/3/library/exceptions.html#NotImplementedError)
        when called.  It need only consist of this line of code:
        `raise NotImplementedError("Concrete subclass of Palette must implement __init__")`
    -   `Palette` provides a placeholder `getColor()` method which raises an
        exception when called.  It consists solely of this statement:
        `raise NotImplementedError("Concrete subclass of Palette must implement getColor() method")`
    -   You are allowed (but not required) to write other methods besides
        `getColor()`.  These methods do not need to raise
        `NotImplementedError`.  These methods would then be available in all
        derived classes of `Palette`.
    -   Concrete subclasses of `Palette` inherit their structure from the
        abstract class `Palette`, and are obligated to provide their own
        implementations of `__init__` and `getColor()` such that they will not
        raise `NotImplementedError` when used.
    -   `getColor(n)` takes an integer as input and returns a string which
        represents a color in this format: `"#RRGGBB"`. This operation is the
        defining characteristic of a  `Palette`  object.
    -   Other data used by `getColor(n)` are supplied through `self`, if needed.
    -   Define at least **two** concrete subclasses of `Palette` classes
        that provide alternative color palettes.  Generalize color palette
        creation so that a user-defined number of iterations may be specified
        instead of using a hard-coded array of colors.
    -   The concrete sub-classes of  `Palette`  are used _interchangeably_ in
        your program.  This is an example of polymorphism in action: objects of
        different classes which are used in the same way.  The code which uses
        a `Palette`-derived object does not inspect the object to determine
        what kind of palette it is; it just works because it defines the
        `getColor()` method.
    -   `Palette` objects have no relation to nor knowledge of `Fractal`.
3.  `PaletteFactory` class or module
    -   Follow the [Factory Method Pattern](https://sourcemaking.com/design_patterns/factory_method)
        in your program when you need to instantiate objects embodying palettes.
        `PaletteFactory` returns a concrete palette object specified by the
        user on the command line.
    -   The file defining `PaletteFactory` is the only place in your entire
        program where your concrete `Palette`-derived classes need to be
        imported.
    -   The `PaletteFactory` itself doesn't have to be an object that you
        instantiate; it can be a function within a module.
        ```
        from PaletteFactory import PaletteFactory

        factory = PaletteFactory()
        palette = factory.makePalette(paletteName)
        ```
        Instead, `PaletteFactory` might be a module containing the function `makePalette()`:
        ```
        import PaletteFactory

        palette = PaletteFactory.makePalette(paletteName)
        ```
    -   When no palette is specified on the command line, `PaletteFactory`
        chooses and returns a default palette.  As the author of this factory,
        you get to decide which type of palette is the default.  This choice is
        _not_ coded into the `main.py` driver program; it is wholly under the
        purview of the factory.
        -   This does not mean that your factory returns a hard-coded array of
            colors; the choice of palette is hard-codde.  Pick from among your
            available color palette classes.
    -   When a non-existent palette is asked for, `NotImplementedError` is raised
        ```
        raise NotImplementedError("Invalid palette requested")
        ```
4.  `ImagePainter` class
    -   Continuing the work of the last sprint, convert this module into a class
        -   This class remains the *only* place in the program where `tkinter` is imported and used directly
    -   The `ImagePainter` constructor takes the products of the `FractalFactory` and `PaletteFactory` as input
        -   Create the `ImagePainter` object in `main.py` **after** the factories have done their thing
        -   The `ImagePainter` does not use or know about the factories; it simply consumes their products
        -   Neither does the `ImagePainter` know about command-line arguments
    -   The `ImagePainter` employs the **Strategy Design Pattern** when it calls a fractal object's `.count()` method
        -   `ImagePainter` does **not** use an `if`/`elif`/`else` decision tree that handles each type of fractal individually
        -   It relies on Duck-Typing to treat all `Fractal`s exactly the same
5.  Documentation (UML, user manual, etc.) from the previous assignment is
    congruent with final the product.  List the names of possible palettes in
    the user manual as this program will not regard absent command line
    arguments as an error and will not print a usage message.
6.  Seven (7) meaningful, non-trivial unit tests are included.  All of them pass.


## Command line interface

The command line interface to your program must follow this format:

```
python src/main.py [FRACTAL_FILE [PALETTE_NAME]]
```

0.  FRACTAL_FILE is the name of a fractal configuration file found in the data directory of the original repository. It is an error if this file name is misspelled, or refers to a file which your program cannot open. It is also an error when this file does not follow the format described below.
1.  PALETTE_NAME is an optional name of a palette which your `PaletteFactory` can produce.

When zero arguments are given, your factories create and return default objects. For example:

```
$ python src/main.py
FractalFactory: Creating default fractal
PaletteFactory: Creating default color palette
```

**IMPORTANT: Because of this behavior, this program *cannot* print a usage message when no arguments are given.**  Instead, users will rely on the user's manual to learn how to run your program.


When only one argument is given, it is used as the name of a fractal configuration file.  A default color palette is chosen by the program:

```
$ python src/main.py data/fulljulia.frac
PaletteFactory: Creating default color palette
```

When two arguments are given, the first is used as the name of a fractal configuration object and the second is the name of a color palette:

```
$ python src/main.py data/funnel-down.frac ColorCube
```

When an missing, or inaccessible fractal configuration file is given, the program may exit with the error raised by `open()`:

```
$ python src/main.py data/NOT_EXIST ColorCube
Traceback (most recent call last):
  File "src/main.py", line 26, in <module>
    fractal = FractalFactory.makeFractal(cfg)
  File "/home/fadein/cs1440-falor-erik-assn4/src/FractalFactory.py", line 30, in makeFractal
    cfg = __readFrac(cfgFile)
  File "/home/fadein/cs1440-falor-erik-assn4/src/FractalFactory.py", line 64, in readFrac
    with open(cfgFile) as f:
FileNotFoundError: [Errno 2] No such file or directory: 'data/NOT_EXIST'
```

**IMPORTANT: Do not hard-code any assumptions about where these files may be found into your program.**


When an invalid palette name is requested, the program exits with an error message

```
$ python src/main.py data/funnel-down.frac NOT_EXIST
Traceback (most recent call last):
  File "src/main.py", line 27, in <module>
    palette = PaletteFactory.makePalette(fractal.iterations, gtype=palette)
  File "/home/fadein/cs1440-falor-erik-assn4/src/PaletteFactory.py", line 49, in makePalette
    raise NotImplementedError("Invalid palette requested")
NotImplementedError: Invalid palette requested
```


## Fractal configuration file format

Fractal configuration files have a simple format.  They are line-oriented
plain-text files with one key/value pair per line.  Key/value pairs are
separated by a colon `:`.  This format is easily converted into dictionaries by
your program.

Study the files in the [../data/](../data/) directory.  Take particular notice
of the file [../data/invalid.frac](../data/invalid.frac), which is an example
of what **NOT** to do!

*   Lines beginning with `#` are comments to be ignored
*   All white space is disregarded
    *   Blank lines are skipped
    *   Strip all white space from the input data
*   Configuration items can appear in *any* order...
    *   ...since you will store them in a dictionary this does not matter
    *   If a configuration item is repeated, the last one overrides what came before
*   The names of configuration items are case-insensitive
    *   UPPERCASE, lowercase, or a MiXtUrE don't matter
    `axislength`  ==  `axisLength` ==  `AXISLENGTH`
    *   Convert all text to lower case as you read it into your program.
*   Item names are separated from their values with a colon `:`
    *   White space around the `:` is *optional*; don't count on it being there
*   The presence of unrecognized or misspelled item names is **NOT** an error
    *   Your program may add these to the dictionary OR ignore them
*   It is an error when items marked **required** below are not present in the configuration file
*   The data type of configuration items used by your program matters
    *   It is an error to supply a value of the wrong type
    *   It is an error to leave a value blank


### Valid items in fractal configuration files

*   `type` - *str* **required**
    *   Informs the program which fractal formula to apply.
    *   For example, this may be `Mandelbrot`, `Julia` or `BurningShipJulia`.
    *   You will define new fractal types that your program can support.
*   `centerX` - *float* **required**
    *   The center point of the image along the X axis.
    *   a.k.a. the "real" axis.
*   `centerY` - *float* **required**
    *   The center point of the image along the Y axis
    *   a.k.a. the "imaginary" axis.
*   `axisLength` - *float* **required**
    *   Defines the size of the square on the complex plane this image covers.
    *   Because the images are square, both axes are the same size.
    *   Making this value smaller results in a *zoomed-in* image.
    *   Making this value larger results in a *zoomed-out* image.
*   `pixels` - *int* **required**
    *   The width (and height) of the image in pixels.
    *   Increasing this parameter increases:
        *   the size of the image.
        *   the amount of detail visible in the image.
        *   the amount of time it takes to generate the image.
*   `iterations` - *int* **required**
    *   The number of iterations the central `for` loop runs before giving up on coloring a pixel.
    *   This is equal to the number of colors in the image.
    *   Increasing this parameter means increasing...
        *   ...the amount of time it takes to render the image
        *   ...the amount detail visible in the image, provided your color palette has enough distinct, contrasting colors
*   `creal` and `cimag` - *float* **optional**
    *   The real and imaginary components of the `C` constant which is used by fractals defined by a variation of the Julia formula.
    *   These items are **required** only for fractals using a variation of the Julia formula.
    *   Your program should raise an error if either of these are missing when `type == julia` or `burningshipjulia`.
    *   These configuration items are ignored by the Mandelbrot forumula.
    *   Experiment with different values to make your Julia set images more interesting.

The meaning of the items within configuration files are illustrated by these images:

#### data/mandelbrot.frac

![mandelbrot-config.png](./mandelbrot-config.png "mandelbrot.frac configuration data diagram")

#### data/mandelbrot-zoomed.frac

![mandelbrot-zoomed-config.png](./mandelbrot-zoomed-config.png "mandelbrot-zoomed.frac configuration data diagram")


### Fractal configuration dictionaries

As your program reads data from a configuration file, it should store the
information into a dictionary.  This dictionary can then easily be passed to
other parts of the program, such as the method that generates the image.

You may find it to be more convenient for your algorithm if the data is first
"conditioned", or converted into a form that is easier to work with.  It is
perfectly acceptible to do this and to store the conditioned data in the same
dictionary.

As an example, upon reading the fractal configuration found in
`data/mandelbrot.frac` my implementation creates a dictionary containing
this information:

```
{
    'type': 'mandelbrot',
    'pixels': 640,
    'axislength': 4.0,
    'iterations': 100,
    'min': {
        'x': -2.0,
        'y': -2.0
    },
    'max': {
        'x': 2.0,
        'y': 2.0
    },
    'pixelsize': 0.00625,
    'imagename': 'mandelbrot.png'
}
```

Note the addition of computed values alongside parameters contained in
the configuration file.

*   The  `min`  and  `max`  values are trivially computed from (`centerX`, `centerY`) and `axisength`, giving the coordinates in the complex plane of the image pixels at the upper left and lower-right corners of the image.
*   Likewise, the length of each pixel of the image in terms of distance on the real and imaginary axes is given as `pixelsize`, which is easily obtained from  `pixels`  and  `axislength`.
*   `imagename` was added by the program for my convenience; you can do the same if it suits you.


### Handling errors in fractal configuration files

-   We will follow the convention that fractal configuration files have the extension .frac, but your program *will not* enforce this.
    -   In other words, your program accepts *any* file *regardless* of its name.
-   Required parameters which are missing are considered an error.
-   Missing or invalid values are likewise to be considered as errors.


[../data/invalid.frac](../data/invalid.frac) is a fractal configuration file which contains errors.  Use it to test that your program can cope with invalid input files.


```
# invalid.frac
#
# This is a purposefully broken fractal config file
# Use this to stress-test your configuration file parser


# Here be dragons!
Type: BurningShipJulia
centerX: in the middle
centerY:
Itertons: 23.654
PIXELS: 894.965
cImag: 0.3
Type: this is redundant
Type: no matter, this will all be forgotten in a moment
Type: julia
```

As explained above, capitalization of text in this file is irrelevant, as are the redundant `Type` parameters.

These are the errors:

-   `centerx`'s value is not a number; the coordinates of the center point are regarded by the program as floats
-   `centery` is missing a value
-   `iterations` was misspelled
    -   The unrecognized item `Itertons` is ignored, which results in `iterations` not being specified at all
-   The value of the `pixels` must be an integer, not a float
-   The required parameter `axislength` is missing
-   The `type` of this fractal is `julia`, but the required `creal` property is missing

When errors are encountered your program must raise a `RuntimeError` with a
message.  To aid debugging, strive to be as specific as you can about what's
wrong:

*   `raise RuntimeError("The value of the 'centerx' parameter is not a number")`
*   `raise RuntimeError("The value of the 'centery' parameter is missing")`
*   `raise RuntimeError("The value of the 'pixels' parameter is not an integer")`
*   `raise RuntimeError("The required parameter 'iterations' is missing")`
*   `raise RuntimeError("The required parameter 'axislength' is missing")`
*   `raise RuntimeError("This is a Julia fractal, but the 'creal' parameter was not specified")`
