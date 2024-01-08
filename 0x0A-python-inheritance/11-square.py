#!/usr/bin/python3
"""
===================================
module with class Square
===================================
"""

Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):
    """Squaree class inherits from Rectangle"""
    def __init__(self, size):
        super().__init__(size, size)


    def __str__(self):
        """
        Returns a string representation of Square
        """
        return "[Square] {}/{}".format(self._Rectangle__width, self._Rectangle__height)
