import unittest
from models.rectangle import Rectangle

class TestRectangleErrors(unittest.TestCase):
    def test_height_non_integer(self):
        with self.assertRaises(TypeError) as context:
            Rectangle(10, "2")
        self.assertEqual(str(context.exception), "height must be an integer")

    def test_width_negative_value(self):
        with self.assertRaises(ValueError) as context:
            r = Rectangle(10, 2)
            r.width = -10
        self.assertEqual(str(context.exception), "width must be > 0")

    def test_x_non_integer(self):
        with self.assertRaises(TypeError) as context:
            r = Rectangle(10, 2)
            r.x = {}
        self.assertEqual(str(context.exception), "x must be an integer")

    def test_y_negative_value(self):
        with self.assertRaises(ValueError) as context:
            Rectangle(10, 2, 3, -1)
        self.assertEqual(str(context.exception), "y must be >= 0")

if __name__ == "__main__":
    unittest.main()
