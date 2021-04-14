import sys
import time
from tkinter import Tk, Canvas, PhotoImage, mainloop


class ImagePainter:
    def __init__(self, size):
        """Set up our PhotoImage and everything else we need to draw our fractal"""
        self.window = Tk()
        self.size = size
        self.img = PhotoImage(width=size, height=size)
        self.canvas = Canvas(self.window, width=size, height=size, bg='#ffffff')
        self.canvas.pack()
        self.canvas.create_image((size/2, size/2), image=self.img, state="normal")

    def paint(self, fractal, palette):
        """Paint a fractal to the screen"""
        before = time.time()


        # Figure out how the boundaries of the PhotoImage relate to coordinates on
        # the imaginary plane.
        minx = fractal.minx
        maxx = fractal.maxx
        miny = fractal.miny

        # At this scale, how much length and height on the imaginary plane does one
        # pixel take?
        pixelsize = abs(maxx - minx) / self.size

        for row in range(self.size, 0, -1):
            for col in range(self.size):
                x = minx + col * pixelsize
                y = miny + row * pixelsize

                iterationCount = fractal.count(complex(x, y))

                color = palette.getColor(iterationCount)
                self.img.put(color, (col, self.size - row))
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
