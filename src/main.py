import sys
import FractalInformation, ImagePainter

if __name__ == '__main__':
    """Here be our main point of entry. At the end of the day, we'll have to determine 
    the user's desired fractal, and pass that information on to ImagePainter.py
    """
    if len(sys.argv) < 2:
        print("Please provide the name of a fractal as an argument")
        for pattern in FractalInformation.dictionary:
            print(pattern)
    desired_fractal = sys.argv[1]
    if desired_fractal not in FractalInformation.dictionary:
        print(f"ERROR: {desired_fractal} is not a valid fractal")
        print("Please choose one of the following:")
        for pattern in FractalInformation.dictionary:
            print(pattern.name)

    fractal = FractalInformation.dictionary[desired_fractal]

    painter = ImagePainter.ImagePainter()
    painter.paint(fractal)
    painter.saveImage(desired_fractal)
