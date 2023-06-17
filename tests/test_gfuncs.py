# %%

import sys, os, unittest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from gfuncpy.gunc import GridFunction, Identity
from gfuncpy.ufunc import *
import unittest
import numpy as np
from math import pi

class GridFunctionTestCase(unittest.TestCase):
    def setUp(self):
        self.x = Identity.uniform_grid(0, 2*pi, 100)
        
    def test_function_operations(self):
        x = self.x

        f1 = sin(x) + cos(x)
        f2 = sin(x) + sin(x) + cos(x)
        f3 = sin(x) + 2
        f4 = 2 + sin(x)
        f5 = sin(x) - 2
        f6 = 2 - sin(x)
        f7 = -sin(x)
        f8 = (sin(x) + cos(x)) / 2
        
        self.assertAlmostEqual(f1(pi/2), np.sin(pi/2) + np.cos(pi/2))
        self.assertAlmostEqual(f2(pi/2), np.sin(pi/2) + np.sin(pi/2) + np.cos(pi/2))
        self.assertAlmostEqual(f3(pi/2), np.sin(pi/2) + 2)
        self.assertAlmostEqual(f4(pi/2), 2 + np.sin(pi/2))
        self.assertAlmostEqual(f5(pi/2), np.sin(pi/2) - 2)
        self.assertAlmostEqual(f6(pi/2), 2 - np.sin(pi/2))
        self.assertAlmostEqual(f7(pi/2), -np.sin(pi/2))
        self.assertAlmostEqual(f8(pi/2), (np.sin(pi/2) + np.cos(pi/2)) / 2)
    
    def test_root(self):
        self.assertRaises(ArithmeticError, lambda: (3 * self.x + 5).root())
        
        # Test for a specific value of pi/2
        root_value = (3 * self.x - 5).root()
        self.assertIsNone(root_value)

if __name__ == '__main__':
    unittest.main()
