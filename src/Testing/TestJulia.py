import unittest
import Fractal
import FractalFactory


class TestJulia(unittest.TestCase):
    def setUp(self):
        fractal_info = {
            "type": "julia",
            "creal": -1,
            "cimag": 0,
            "pixels": 1024,
            "centerx": 0.0,
            "centery": 0.0,
            "axislength": 4.0,
            "iterations": 78
        }
        self.default_julia = FractalFactory.makeFractal(fractal_info)

    def test_inheritance(self):
        self.assertTrue(type(self.default_julia), Fractal.Fractal)

    def test_count(self):
        self.assertIsInstance(self.default_julia.count(complex(0, 0)), int)


if __name__ == '__main__':
    unittest.main()
