import unittest
from mbrot_fractal import colorOfThePixel, palette, MAX_ITERATIONS, pixelsWrittenSoFar


# autocmd BufWritePost <buffer> !python3 runTests.py

class TestMandelbrot(unittest.TestCase):
    def test_colorOfThePixel(self):
        self.assertEqual(colorOfThePixel(complex(0, 0), palette), '#e8283f')
        self.assertEqual(colorOfThePixel(complex(-0.751, 1.1075), palette), '#baf12e')
        self.assertEqual(colorOfThePixel(complex(-0.2, 1.1075), palette), '#e0ceaf')
        self.assertEqual(colorOfThePixel(complex(-0.75, 0.1075), palette), '#f1da2e')
        self.assertEqual(colorOfThePixel(complex(-0.748, 0.1075), palette), '#deb69f')
        self.assertEqual(colorOfThePixel(complex(-0.7562500000000001, 0.078125), palette), '#e1bc7e')
        self.assertEqual(colorOfThePixel(complex(-0.7562500000000001, -0.234375), palette), '#e7ddd7')
        self.assertEqual(colorOfThePixel(complex(0.3374999999999999, -0.625), palette), '#e1d1bd')
        self.assertEqual(colorOfThePixel(complex(-0.6781250000000001, -0.46875), palette), '#eccd43')
        self.assertEqual(colorOfThePixel(complex(0.4937499999999999, -0.234375), palette), '#d9e758')
        self.assertEqual(colorOfThePixel(complex(0.3374999999999999, 0.546875), palette), '#e1cbbd')

    def test_pixelsWrittenSoFar(self):
        self.assertEqual(pixelsWrittenSoFar(7, 7), 49)
        self.assertEqual(pixelsWrittenSoFar(257, 321), 82497)
        self.assertEqual(pixelsWrittenSoFar(256, 256), 65536)
        self.assertEqual(pixelsWrittenSoFar(100, 100), 10000)
        self.assertEqual(pixelsWrittenSoFar(640, 480), 307200)

    def test_palleteLength(self):
        self.assertEqual(111, len(palette))


if __name__ == '__main__':
    unittest.main()
