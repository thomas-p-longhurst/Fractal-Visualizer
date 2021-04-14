import PaletteDefault, PaletteBlackAndWhite, PaletteTrippy


def makePalette(palette_name):
    """Returns a concrete palette object specified by a String."""
    if palette_name == "default":
        palette = PaletteDefault.PaletteDefault()
    elif palette_name == "black_and_white":
        palette = PaletteBlackAndWhite.PaletteBlackAndWhite()
    elif palette_name == "trippy":
        palette = PaletteTrippy.PaletteTrippy()
    else:
        raise NotImplementedError("Invalid palette requested")
    return palette
