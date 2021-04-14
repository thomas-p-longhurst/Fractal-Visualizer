from Palette import Palette
from colour import Color


class PaletteDefault(Palette):
    def __init__(self):
        yellow = Color('yellow')
        green = Color('green')
        blue = Color('blue')
        black = Color('black')

        color_step = 10

        self.__color_palette = [c.hex_l for c in yellow.range_to(green, color_step)]
        self.__color_palette += [c.hex_l for c in green.range_to(blue, color_step)][1:]
        self.__color_palette += [c.hex_l for c in blue.range_to(black, color_step)][1:]

    def getColor(self, iterationCount):
        return self.__color_palette[iterationCount % len(self.__color_palette)]

