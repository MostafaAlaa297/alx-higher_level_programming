#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):

    def test_max_integer(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
        self.assertEqual(max_integer([1, -2, 3, -4]), 3)
        self.assertEqual(max_integer([5, 2, 5, 1]), 5)
        self.assertEqual(max_integer([42]), 42)
        self.assertEqual(max_integer([1.5, 2.5, 3.5]), 3.5)

    def test_errors(self):
        self.assertIsNone(max_integer([]))
        with self.assertRaises(TypeError):
            max_integer(["not_a_list", 1])
        self.assertRaises(TypeError, max_integer, [2, [2, 1]]) # Another way to test type error

if __name__ == '__main__':
    unittest.main()
