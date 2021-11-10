import unittest
import Fractal
import FractalFactory


class TestMandelbrot(unittest.TestCase):
    def setUp(self):
        fractal_info = {
            "type": "mandelbrot",
            "pixels": 640,
            "centerx": 0.0,
            "centery": 0.0,
            "axislength": 4.0,
            "iterations": 100
        }
        self.default_mandelbrot = FractalFactory.makeFractal(fractal_info)

    def test_inheritance(self):
        self.assertTrue(type(self.default_mandelbrot), Fractal.Fractal)

    def test_count(self):
        self.assertIsInstance(self.default_mandelbrot.count(complex(0, 0)), int)


if __name__ == '__main__':
    unittest.main()
