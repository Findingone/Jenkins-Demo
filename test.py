#!/usr/bin/python3

import unittest
from build import *

class SampleTest(unittest.TestCase):
    def test_addition(self):
        a = 10
        b = 15
        expected = 25
        self.assertEqual(addition(a, b), expected)
    def test_subtraction(self):
        a = 20
        b = 18
        expected = 2
        self.assertEqual(subtraction(a, b), expected)
    def test_multiplication(self):
        a = 5
        b = 6
        expected = 30
        self.assertEqual(multiplication(a, b), expected)
    def test_division(self):
        a = 100
        b = 20
        expected = 5
        self.assertEqual(division(a, b), expected)
    
if __name__ == '__main__':
    unittest.main()
