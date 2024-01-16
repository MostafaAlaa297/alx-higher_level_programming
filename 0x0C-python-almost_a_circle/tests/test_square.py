#!/usr/bin/python3
"""
Unit tests for the square
"""
import unittest
from models.square import

import unittest
from models.square import Square

class TestSquare(unittest.TestCase):
    def test_default_id_increment(self):
        s1 = Square(5)
        s2 = Square(10)
        s3 = Square(15)

        self.assertEqual(s1.id, 1)
        self.assertEqual(s2.id, 2)
        self.assertEqual(s3.id, 3)

    def test_custom_id(self):
        s4 = Square(20, id=12)
        self.assertEqual(s4.id, 12)

    def test_default_id_after_custom_id(self):
        Square._Base__nb_objects = 0  # Reset the counter for testing purposes
        s5 = Square(25)
        self.assertEqual(s5.id, 1)

    def test_size_property(self):
        s = Square(30)
        self.assertEqual(s.size, 30)

    def test_size_property_setter(self):
        s = Square(35)
        s.size = 40
        self.assertEqual(s.size, 40)
        self.assertEqual(s.width, 40)
        self.assertEqual(s.height, 40)

    def test_update_method(self):
        s = Square(45)
        s.update(1, 50, 5, 10)
        self.assertEqual(s.id, 1)
        self.assertEqual(s.size, 50)
        self.assertEqual(s.x, 5)
        self.assertEqual(s.y, 10)

    def test_update_method_kwargs(self):
        s = Square(55)
        s.update(id=2, size=60, x=15, y=20)
        self.assertEqual(s.id, 2)
        self.assertEqual(s.size, 60)
        self.assertEqual(s.x, 15)
        self.assertEqual(s.y, 20)

    def test_str_method(self):
        s = Square(65)
        self.assertEqual(str(s), "[Square] (1) 0/0 - 65")

    def test_to_dictionary_method(self):
        s = Square(70, 5, 10, 1)
        dictionary = s.to_dictionary()
        expected_dict = {'id': 1, 'size': 70, 'x': 5, 'y': 10}
        self.assertEqual(dictionary, expected_dict)

if __name__ == "__main__":
    unittest.main()
