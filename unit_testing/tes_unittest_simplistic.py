from unit_testing.simplecalc import SimpleCalc
import unittest


# Class that inherits from TestCase

class CalcTests(unittest.TestCase):
    calc = SimpleCalc()

    def setUp(self):
        self.calc = SimpleCalc()
        print("Setting up")

    def test_add(self):
        actual = self.calc.add(4, 2)
        expected = 6
        self.assertEqual(actual, expected)

    def test_subtract(self):
        actual = self.calc.sub(4, 2)
        expected = 2
        self.assertEqual(actual, expected)

    def test_multiply(self):
        actual = self.calc.multi(4, 2)
        expected = 8
        self.assertEqual(actual, expected)

    def test_division(self):
        actual = self.calc.divide(4, 2)
        expected = 2
        self.assertEqual(actual, expected)

# use print statements to see why it might fail
