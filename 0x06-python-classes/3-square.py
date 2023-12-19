#!/usr/bin/python3
"""2-square.py"""
class Square:
    """
    Defines a square.

    Attributes:
        __size (int): The size of the square
    """
    def __init__(self, size=0):
        """
        Initializes a new square instance

        Args:
        size (int, optional): The size of the square. Defaults to 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
        self._area = size ** 2

    def area(self):
        return self._area
