# test_simple_calculator.py

import unittest
from simple_calculator import SimpleCalculator


class TestSimpleCalculator(unittest.TestCase):
    """Unit tests for the SimpleCalculator class."""

    def setUp(self):
        """Set up a SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    # Test addition
    def test_addition(self):
        """Test addition method."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(0, 0), 0)
        self.assertEqual(self.calc.add(-2, -3), -5)
        self.assertAlmostEqual(self.calc.add(2.5, 3.1), 5.6)

    # Test subtraction
    def test_subtraction(self):
        """Test subtraction method."""
        self.assertEqual(self.calc.subtract(5, 3), 2)
        self.assertEqual(self.calc.subtract(3, 5), -2)
        self.assertEqual(self.calc.subtract(0, 0), 0)
        self.assertEqual(self.calc.subtract(-2, -3), 1)
        self.assertAlmostEqual(self.calc.subtract(5.5, 2.2), 3.3)

    # Test multiplication
    def test_multiplication(self):
        """Test multiplication method."""
        self.assertEqual(self.calc.multiply(2, 3), 6)
        self.assertEqual(self.calc.multiply(-2, 3), -6)
        self.assertEqual(self.calc.multiply(0, 5), 0)
        self.assertEqual(self.calc.multiply(-2, -3), 6)
        self.assertAlmostEqual(self.calc.multiply(2.5, 4), 10.0)

    # Test division
    def test_division(self):
        """Test division method."""
        self.assertEqual(self.calc.divide(6, 3), 2)
        self.assertEqual(self.calc.divide(-6, 3), -2)
        self.assertEqual(self.calc.divide(5, 2), 2.5)
        # Division by zero should return None
        self.assertIsNone(self.calc.divide(10, 0))
        self.assertAlmostEqual(self.calc.divide(7.5, 2.5), 3.0)


if __name__ == "__main__":
    unittest.main()
