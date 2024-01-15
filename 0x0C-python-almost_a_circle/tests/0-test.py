#!/usr/bin/python3

import unittest
from models.base import Base

class TestBase(unittest.TestCase):
    def setUp(self):
        Base._Base__nb_objects = 0

    def test_default_id_increment(self):
        b1 = Base()
        b2 = Base()
        b3 = Base()

        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 3)

    def test_custome_id(self):
        b4 = Base(12)
        self.assertEqual(b4.id, 12)

    def test_default_id_after_custom_id(self):
        b5 = Base()
        self.assertEqual(b5.id, 1)

if __name__ == "__main__":
    unittest.main()

