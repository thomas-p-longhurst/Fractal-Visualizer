import unittest

from Testing import TestMandelbrot, TestJulia, TestPalette


suite = unittest.TestSuite()
tests = (TestMandelbrot.TestMandelbrot, TestJulia.TestJulia, TestPalette.TestPalette)
for test in tests:
    suite.addTest(unittest.makeSuite(test))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(suite)
