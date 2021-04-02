import sys
import time
import Mandelbrot, Julia, Palette
from tkinter import Tk, Canvas, PhotoImage, mainloop


class ImagePainter:
    def __init__(self):
        """Set up our PhotoImage and everything else we need to draw our fractal"""
        self.window = Tk()
        self.img = PhotoImage(width=512, height=512)
        self.canvas = Canvas(self.window, width=512, height=512, bg='#ffffff')
        self.canvas.pack()
        self.canvas.create_image((256, 256), image=self.img, state="normal")

    def paint(self, fractal):
        """Paint a fractal to the screen"""
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

                if fractal['type'] == "mandelbrot":
                    iterationCount = Mandelbrot.getIterationCount(complex(x, y), Palette.getLen())
                # elif fractal['type'] == "Julia":
                else:
                    iterationCount = Julia.getIterationCount(complex(x, y), Palette.getLen())

                color = Palette.getColor(iterationCount)
                self.img.put(color, (col, 512 - row))
            self.window.update()  # display a row of pixels


        # Save the image as a PNG
        after = time.time()
        print(f"Done in {after - before:.3f} seconds!", file=sys.stderr)

    def saveImage(self, fractal_name):
        """Given a file path, save the image to the disk"""
        self.img.write(f"{fractal_name}.png")
        print(f"Wrote image {fractal_name}.png")

        # Call tkinter.mainloop so the GUI remains open
        print("Close the image window to exit the program")
        mainloop()
