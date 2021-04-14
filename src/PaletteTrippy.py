from Palette import Palette
from colour import Color


class PaletteTrippy(Palette):
    def __init__(self):
        red = Color('red')
        steelblue = Color('steelblue')
        orange = Color('orange')
        navy = Color('navy')
        yellow = Color('yellow')
        darkmagenta = Color('darkmagenta')
        green = Color('green')
        orangered = Color('orangered')
        blue = Color('blue')
        gold = Color('gold')
        purple = Color('purple')
        greenyellow = Color('greenyellow')
        black = Color('black')

        color_step = 2

        self.__color_palette = [c.hex_l for c in red.range_to(steelblue, color_step)]
        self.__color_palette += [c.hex_l for c in steelblue.range_to(orange, color_step)][1:]
        self.__color_palette += [c.hex_l for c in orange.range_to(navy, color_step)][1:]
        self.__color_palette += [c.hex_l for c in navy.range_to(yellow, color_step)][1:]
        self.__color_palette += [c.hex_l for c in yellow.range_to(darkmagenta, color_step)][1:]
        self.__color_palette += [c.hex_l for c in darkmagenta.range_to(green, color_step)][1:]
        self.__color_palette += [c.hex_l for c in green.range_to(orangered, color_step)][1:]
        self.__color_palette += [c.hex_l for c in orangered.range_to(blue, color_step)][1:]
        self.__color_palette += [c.hex_l for c in blue.range_to(gold, color_step)][1:]
        self.__color_palette += [c.hex_l for c in gold.range_to(purple, color_step)][1:]
        self.__color_palette += [c.hex_l for c in purple.range_to(greenyellow, color_step)][1:]
        self.__color_palette += [c.hex_l for c in greenyellow.range_to(black, color_step)][1:]


    def getColor(self, iterationCount):
        return self.__color_palette[iterationCount % len(self.__color_palette)]

    def getLen(self):
        return len(self.__color_palette)