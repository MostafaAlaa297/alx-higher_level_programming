import unittest
from models.rectangle import Rectangle

class TestRectangleCreation(unittest.TestCase):
    def setUp(self):
        # Reset the Base class __nb_objects attribute before each test
        Rectangle._Base__nb_objects = 0

    def test_default_id_increment(self):
        r1 = Rectangle(10, 2)
        r2 = Rectangle(2, 10)

        self.assertEqual(r1.id, 1)
        self.assertEqual(r2.id, 2)

    def test_custom_id(self):
        r3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r3.id, 12)

if __name__ == "__main__":
    unittest.main()
