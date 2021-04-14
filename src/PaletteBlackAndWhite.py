from Palette import Palette
from colour import Color


class PaletteBlackAndWhite(Palette):
    def __init__(self):
        black = Color('black')
        white = Color('white')

        color_step = 2

        self.__color_palette = [c.hex_l for c in black.range_to(white, color_step)]

    def getColor(self, iterationCount):
        return self.__color_palette[iterationCount % len(self.__color_palette)]
