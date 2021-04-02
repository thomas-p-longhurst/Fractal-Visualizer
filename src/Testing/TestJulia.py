import unittest
from Testing.julia_fractal import getNumber, getColorFromPalette
from Julia import getIterationCount
import Palette
from Palette import getLen


# autocmd BufWritePost <buffer> !python3 runTests.py

class TestJulia(unittest.TestCase):
    def test_numberOfIterations(self):
        self.assertEqual(getNumber(complex(0, 0)), getIterationCount(complex(0, 0), getLen()))
        self.assertEqual(getNumber(complex(-0.751, 1.1075)), getIterationCount(complex(-0.751, 1.1075), getLen()))
        self.assertEqual(getNumber(complex(-0.2, 1.1075)), getIterationCount(complex(-0.2, 1.1075), getLen()))
        self.assertEqual(getNumber(complex(-0.75, 0.1075)), getIterationCount(complex(-0.75, 0.1075), getLen()))
        self.assertEqual(getNumber(complex(-0.748, 0.1075)), getIterationCount(complex(-0.748, 0.1075), getLen()))
        self.assertEqual(getNumber(complex(-0.7562500000000001, 0.078125)), getIterationCount(complex(-0.7562500000000001, 0.078125), getLen()))
        self.assertEqual(getNumber(complex(-0.7562500000000001, -0.234375)), getIterationCount(complex(-0.7562500000000001, -0.234375), getLen()))
        self.assertEqual(getNumber(complex(0.3374999999999999, -0.625)), getIterationCount(complex(0.3374999999999999, -0.625), getLen()))
        self.assertEqual(getNumber(complex(-0.6781250000000001, -0.46875)), getIterationCount(complex(-0.6781250000000001, -0.46875), getLen()))
        self.assertEqual(getNumber(complex(0.4937499999999999, -0.234375)), getIterationCount(complex(0.4937499999999999, -0.234375), getLen()))
        self.assertEqual(getNumber(complex(0.3374999999999999, 0.546875)), getIterationCount(complex(0.3374999999999999, 0.546875), getLen()))

    def test_colorOfThePixel(self):
        self.assertEqual(getColorFromPalette(complex(0, 0)), Palette.getColor(getIterationCount(complex(0, 0), getLen())))
        self.assertEqual(getColorFromPalette(complex(-0.751, 1.1075)), Palette.getColor(getIterationCount(complex(-0.751, 1.1075), getLen())))
        self.assertEqual(getColorFromPalette(complex(-0.2, 1.1075)), Palette.getColor(getIterationCount(complex(-0.2, 1.1075), getLen())))
        self.assertEqual(getColorFromPalette(complex(-0.75, 0.1075)), Palette.getColor(getIterationCount(complex(-0.75, 0.1075), getLen())))
        self.assertEqual(getColorFromPalette(complex(-0.748, 0.1075)), Palette.getColor(getIterationCount(complex(-0.748, 0.1075), getLen())))
        self.assertEqual(getColorFromPalette(complex(-0.7562500000000001, 0.078125)), Palette.getColor(getIterationCount(complex(-0.7562500000000001, 0.078125), getLen())))
        self.assertEqual(getColorFromPalette(complex(-0.7562500000000001, -0.234375)), Palette.getColor(getIterationCount(complex(-0.7562500000000001, -0.234375), getLen())))
        self.assertEqual(getColorFromPalette(complex(0.3374999999999999, -0.625)), Palette.getColor(getIterationCount(complex(0.3374999999999999, -0.625), getLen())))
        self.assertEqual(getColorFromPalette(complex(-0.6781250000000001, -0.46875)), Palette.getColor(getIterationCount(complex(-0.6781250000000001, -0.46875), getLen())))
        self.assertEqual(getColorFromPalette(complex(0.4937499999999999, -0.234375)), Palette.getColor(getIterationCount(complex(0.4937499999999999, -0.234375), getLen())))
        self.assertEqual(getColorFromPalette(complex(0.3374999999999999, 0.546875)), Palette.getColor(getIterationCount(complex(0.3374999999999999, 0.546875), getLen())))



if __name__ == '__main__':
    unittest.main()
