# test_calculator.py

import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        # This method is run before each test, useful for setup code.
        self.calc = Calculator()

    def test_arae_circle(self):
        # Test addition functionality
        result = self.calc.area_circle(3)
        self.assertEqual(result, 28.26)
        
        result = self.calc.area_circle(2)
        self.assertEqual(result, 12.56)
        
        result = self.calc.area_circle(-1)
        self.assertEqual(result, 3.14)


if __name__ == '__main__':
    unittest.main()
