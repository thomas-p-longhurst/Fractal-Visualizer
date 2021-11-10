import unittest
import PaletteFactory
import Palette
from colour import Color


class TestPalette(unittest.TestCase):
    def setUp(self):
        self.default_palette = PaletteFactory.makePalette("default")
        self.black_and_white_palette = PaletteFactory.makePalette("black_and_white")
        self.trippy_palette = PaletteFactory.makePalette("trippy")

    def test_inheritance(self):
        self.assertTrue(issubclass(type(self.default_palette), Palette.Palette))
        self.assertTrue(issubclass(type(self.black_and_white_palette), Palette.Palette))
        self.assertTrue(issubclass(type(self.trippy_palette), Palette.Palette))

    def test_color_type(self):
        self.assertIsInstance(self.default_palette.getColor(0), str)
        self.assertIsInstance(self.black_and_white_palette.getColor(0), str)
        self.assertIsInstance(self.trippy_palette.getColor(0), str)

    def test_color_value(self):
        self.assertEquals(self.black_and_white_palette.getColor(0), '#000000')
        self.assertEquals(self.black_and_white_palette.getColor(1), '#ffffff')
        self.assertEquals(self.black_and_white_palette.getColor(2), '#000000')
        self.assertEquals(self.black_and_white_palette.getColor(3), '#ffffff')
        self.assertEquals(self.black_and_white_palette.getColor(4), '#000000')

if __name__ == '__main__':
    unittest.main()
