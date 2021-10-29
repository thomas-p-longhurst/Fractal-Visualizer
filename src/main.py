#!/usr/bin/env python3

import sys

import julia_fractal as julia
import mbrot_fractal


JULIAS = [ 'fulljulia', 'hourglass', 'lace-curtains', 'lakes' ]
MBROTS = [ 'elephants', 'leaf', 'mandelbrot', 'mandelbrot-zoomed', 'seahorse', 'spiral0', 'spiral1', 'starfish' ]

# quit when too many arguments are given
if len(sys.argv) < 2:
    print("Please provide the name of a fractal as an argument")
    for i in JULIAS + MBROTS:
        print(f"\t{i}")
    sys.exit(1)

# quite when one of the arguments isn't in the command line
elif sys.argv[1] not in JULIAS + MBROTS:
    print(f"ERROR: {sys.argv[1]} is not a valid fractal")
    print("Please choose one of the following:")
    all_of_the_fractals = JULIAS
    all_of_the_fractals.extend(MBROTS)
    for i in all_of_the_fractals:
        print(f"\t{i}")
    sys.exit(1)

# Otherwise, quit with an error message to help the user learn how to run it
else:
    # fractal is the 1st argument after the program name
    fracal = sys.argv[1]
    if sys.argv[1] in JULIAS:
        julia.julia_main(sys.argv[1])
    elif sys.argv[1] in MBROTS:
        fratcal = sys.argv[1]
        mbrot_fractal.mbrot_main(fratcal)
        
