# Code Smells Report

## Instructions

Edit this file and include it in your submission.

For each instance of a code smell you find in the starter code report:

*	Where you found it (filename + line number)
*	Copy the offensive code
*	Explain why the smell is a problem
*	Describe how you fixed it

These are the code smells that you can expect to find in the starter code.

0.  Dead Code
    * A variable, parameter, field, method or class is no longer used (usually because it is obsolete)
1.  Magic Numbers
    * Numeric literals that appear in critical places but without any apparent meaning
    * "When I see the number `214` here, does it have the same meaning as the `214` over there?"
2.  Global Variables
    * A global is being used to avoid passing a parameter into a function
    * A global is being used to return an extra value from a function
3.  TMI Comments (Too Much Information)
    * A function or method is filled with many explanatory comments
4.  Too Long Parameter List
    * More than three or four parameters for a method
5.  Too Long Function/Method
    * A method contains too many lines of code
    * Generally, any method longer than ten lines should make you start asking questions
6.  Complex decision trees
    * Long or deeply nested trees of `if/elif/else`
    * Complex `switch` operators
7.  Shotgun Surgery
    * Making any modifications requires that you make many small changes to many different functions/classes
8.  Alternative Classes/Functions with Different Interfaces
    * Two classes perform identical functions but have different method names
    * Two functions perform identical functions but have different names
    * Two functions perform identical functions but take different parameters
9.  Spaghetti Code
    * Lots of meandering code without a clear goal
    * Many functions/objects used in inconsistent ways
    * All code is contained in one giant function/method with huge `if/else` branches
    * "It would be easier to rewrite this than to understand it"

Other code smells may also be identified; list them as well.


## Smells

### `main.py`
#### Lengthy Code
Lines 18-20:
```python
all_of_the_fractals = MBROTS
all_of_the_fractals.extend(JULIAS)
for i in all_of_the_fractals:
```
Not super offensive, but not too great to read.

This can very easily be shortened to:
```python
for i in MBROTS + JULIAS:
```
This is easier to read, and shortens the code.

#### Unused Variable
Lines 24-30:
```python
else:
    fracal = sys.argv[1]
    if sys.argv[1] in JULIAS:
        julia_fractal.julia_main(sys.argv[1])
    elif sys.argv[1] in MBROTS:
        fratcal = sys.argv[1]
        mbrot_fractal.mbrot_main(fratcal)
```
`fracal` and `fratcal` are both typoes, and `fracal` is never used. Additionally, these two variables
have the exact same value. Finally, the code will be easier to understand if instances of `sys.argv[1]` are
given a variable name. Consider the following:
```python
else:
    fractal = sys.argv[1]
    if fractal in JULIAS:
        julia_fractal.julia_main(fractal)
    elif fractal in MBROTS:
        mbrot_fractal.mbrot_main(fractal)
```

### `julia_fractal.py`
#### Unhelpful variable name
Lines 14-15:
```python
# c is the Julia Constant; varying this value can yield interesting images
c = complex(-1.0, 0.0)
```
"c" doesn't give us any idea what the variable is. Give it a more descriptive name:
```python
# julia_constant is the Julia Constant; varying this value can yield interesting images
julia_constant = complex(-1.0, 0.0)
```

#### Global Variables
Lines 17-20:
```python
# I feel bad about all of the global variables I'm using.
# There must be a better way...
global grad
global win
```
Rather than having tons of globals defined all over the place, we should make this file into a class and
have these as attributes that are defined in the constructor.

#### This for loop stinks
Lines 22-30
```python
# Here 76 refers to the number of colors in the palette
for i in range(78):
    z = z * z + c  # Iteratively compute z1, z2, z3 ...
    if abs(z) > 2:
        return grad[i]  # The sequence is unbounded
        z += z + c
# TODO: One of these return statements makes the program crash sometimes
return grad[77]         # Else this is a bounded sequence
return grad[78]
```
In the comment, it mentions the number 76. The number 76 is nowhere to be seen. Additionally, the loop will
always run 78 times, regardless of if we change our palette. `z` is not very descriptive, but since it's
used in the wikipedia page for the mandelbrodt set, I'll let it slide. Finally, lines 27 and 30 are simply 
unreachable.

In the end, we should have something like this:
```python
for color in grad:
    z = z * z + c  # Iteratively compute z1, z2, z3 ...
    if abs(z) > 2:
        return color  # The sequence is unbounded
return grad[77]         # Else this is a bounded sequence
```

#### Longest function name I've ever seen in my life
Lines 33-41:
```python
def getFractalConfigurationDataFromFractalRepositoryDictionary(dictionary, name):
    """Make sure that the fractal configuration data repository dictionary
    contains a key by the name of 'name'

    When the key 'name' is present in the fractal configuration data repository
    dictionary, return its value.

    Return False otherwise
    """
```
This is basically word-vomit. Also, why would we return a boolean value? Try this:
```python
def getFractalData(dicitonary, name):
    """Returns the value of 'name' as found in 'dictionary'. Returns None if
    'name' is not in 'dictionary'.    
    """
```

#### Superfluous for loop
Lines 42-46
```python
for key in dictionary:
    if key in dictionary:
        if key == name:
            value = dictionary[key]
            return key
```
We don't need to iterate over a dictionary. Replace this entire loop with:
```python
if name in dictionary:
    return dictionary[name]
return None
```

#### Useless code
Line 49:
```python
photo = None
```
Global variable initialization. Should be put in class constructor 

#### Janky function stub
Lines 51-53:
```python
def makePicture(f, i, e):
    """Paint a Fractal image into the TKinter PhotoImage canvas.
    Assumes the image is 512x512 pixels."""
```
What do those parameters mean? `f` is the only one that's used, `i` and `e` are not referenced.
Also, I feel like we shouldn't assume the size of the image. Change `f` to be more descriptive, and replace
`i` and `e` with `width` and `height`, giving default values.

#### More global variables
Lines 55-57:
```python
global win
global grad
global photo
```
and line 67:
```python
global WHITE
```
Again, we should be changing this file to a class that has these as attributes. `WHITE` may want to be 
defined in the palette.

#### Function's doing too much
Lines 68-77:
```python
    # Display the image on the screen
    canvas = Canvas(win, width=512, height=512, bg=WHITE)
    canvas.pack()
    # TODO: Sometimes I wonder whether some of my functions are trying to do
    #       too many different things... this is the correct part of the
    #       program to create a GUI window, right?
    canvas.create_image((256, 256), image=photo, state="normal")
    canvas.pack()  # This seems repetitive
    canvas.pack()  # But it is how Larry wrote it
    canvas.pack()  # Larry's a smart guy.  I'm sure he has his reasons.
```
This is not the correct part of the program to create a GUI window. This should be put into its own function
called `makeGUI()` or something like that. Also, I'm not sure where we need to call `canvas.pack()`, but
I do know we don't need to call it 6 times in the same method.

#### Unused variables
Line 79:
```python
area_in_pixels = 512 * 512
```
and Line 87:
```python
fraction = int(512 / 64)
```
are never used. Not sure where we'd use them either, so safe delete.

#### Unhelpful argument names
Line 156:
```python
def julia_main(i):
```
`i` is the name of the fractal design as a String. The name should reflect this.

Line 161:
```python
b4 = time()
```
1337speak is not tolerable in the year of our lord 2021.


#### Two identical method calls
Line 169-171:
```python
photo.write(i + ".png")
print("Wrote picture " + i + ".png")
photo.write(i + ".png")
```
Doesn't seem like we need to write a photo to the disk twice. Delete the second one.

### `mbrot_fractal.py`
#### Utterly astounding global values
Lines 34-35:
```python
seven = 7.0
TWO = sqrt(4)
```
Is it really that hard to remember two numbers? Delete these and replace their uses with the regular 
numbers.

#### Less-than-stellar method name
Line 40:
```python
def colorOfThePixel(c, palette):
```
It returns something, so the name should be called `getColor()`, or something to that effect.

#### Global usage
Lines 42-46:
```python
global z
z = complex(0, 0)  # z0

global MAX_ITERATIONS
global i
```
`z` should be passed to the method as an argument, `MAX_ITERATIONS` should be done in the class's 
constructor, and declaring `i` as a global may actually harm the program, as it is used as a variable
in future for loops.

#### Dead return statements
Lines 55-56:
```python
return palette[MAX_ITERATIONS - 1]   # Indicate a bounded sequence
return palette[MAX_ITERATIONS]
```
The second is unreachable. Delete it.

#### Wacky function
Lines 61-68:
```python
def paint(fractals, imagename):
    """Paint a Fractal image into the TKinter PhotoImage canvas.
    This code creates an image which is 640x640 pixels in size."""

    global palette
    global img

    fractal = fractals[imagename]
```
I feel we shouldn't be locked into a 640x640 image. Pass width and height into arguments. `palette` and
`img` should either be passes as arguments or declared in class constructor. It also seems that the image
created is 512x512 and not 640x640. Finally, `fractals` and `imagename` can be condensed into a single
argument, since line 68 is the only place they're used.

#### Doing too much
Lines 77-80:
```python
# Display the image on the screen
canvas = Canvas(window, width=512, height=512, bg='#ffffff')
canvas.pack()
canvas.create_image((256, 256), image=img, state="normal")
```
Our canvas should be created elsewhere, and passed into this method as an argument.

#### Unused variables
Line 75:
```python
maxy = fractal['centerY'] + (fractal['axisLen'] / 2.0)
```
and Lines 86-87:
```python
portion = int(512 / 64)
total_pixels = 1048576
```
Are never used. Nevermind the fact that the latter two use some magic numbers.