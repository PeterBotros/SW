# test_calculator.py

import unittest
from calculator import Areacircle

class TestCalculator(unittest.TestCase):

    def setUp(self):
        # This method is run before each test, useful for setup code.
        self.calc = Areacircle()

    def test_add(self):
        # Test addition functionality
        result = self.calc.area(3)
        self.assertEqual(result, 28.26)
        
        result = self.calc.area(0)
        self.assertEqual(result, 0)
        
        result = self.calc.area(-1)
        self.assertEqual(result, 3.14)


if __name__ == '__main__':
    unittest.main()
