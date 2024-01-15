#!/usr/bin/python3

import unittest
from models.rectangle import Rectangle

class TestRectangleArea(unittest.TestCase):
    
    def test_area_case1(self):
        r1 = Rectangle(3, 2)
        self.assertEqual(r1.area(), 6)

    def test_area_case2(self):
        r2 = Rectangle(2, 10)
        self.asserEqual(r2.area(), 20)

    def test_area_case3(self):
        r3 = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(r3.area(), 56)

if __name__ = "__main__":
    unittest.main()
