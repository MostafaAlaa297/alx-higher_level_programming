#!/usr/bin/python3
"""
Unit tests for the rectangle module
"""

import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """test cases for the rectangle module"""
    def test_attributes(self):
        """The attributes"""
        r = Rectangle(10, 5, 2, 7, 1)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 5)
        self.assertEqual(r.x, 2)
        self.assertEqual(r.y, 7)
        self.assertEqual(r.id, 1)

    def test_invalid_width(self):
        """Test invalid_width"""
        with self.assertRaises(ValueError):
            r = Rectangle(-5, 5, 2, 7, 1)
    
    def test_invalid_height(self):
        """Test incalid height"""
        with self.assertRaises(ValueError):
            r = Rectangle(10, -5, 2, 7, 1)

    def test_invalid_x(self):
        """Test invalid x"""
        with self.assertRaises(ValueError):
            r = Rectangle(10, 5, -2, 7, 1)

    def test_invalid_y(self):
        """Test invalid y"""
        with self.assertRaises(ValueError):
            r = Rectangle(10, 5, 2, -7, 1)

    def test_area(self):
        """Test area()"""
        r = Rectangle(5, 6)
        self.assertEqual(r.area(), 30)

    def test_display(self):
        """Test, display"""
        r = Rectangle(2, 3)
        self.assertEqual(r.display(), None)

    def test_update(self):
        """Test update"""
        r = Rectangle(10, 5, 2, 7, 1)
        r.update(2, 8, 4, 1, 3)
        self.assertEqual(r.width, 8)
        self.assertEqual(r.height, 4)
        self.assertEqual(r.x, 1)
        self.assertEqual(r.y, 3)
        self.assertEqual(r.id, 2)

    def test_todictionary(self):
        """Test todictionary"""
        r = Rectangle(10,5, 2, 7, 1)
        r_dict = r.to_dictionary()
        self.assertEqual(r_dict, {"id": 1, "width": 10, "height": 5, "x": 2, "y": 7})

    def test_str(self):
        """returning string"""
        r = Rectangle(10, 5, 2, 7, 1)
        self.assertEqual(str(r), "[Rectangle] (1) 2/7 - 10/5")

if __name__ == "__main__":
    unittest.main()
