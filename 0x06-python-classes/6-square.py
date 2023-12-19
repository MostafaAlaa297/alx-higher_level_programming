#!/usr/bin/python3
"""5-square.py"""
class Square:
    """
    Defines a square.

    Attributes:
        __size (int): The size of the square
    """
    def __init__(self, size=0, position=(0, 0)):
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

        if not isinstance(position, tuple) or len(position) != 2 or \
           not isinstance(position[0], int) or not isinstance(position[1], int) or \
           position[0] < 0 or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position

    @property
    def size(self):
        """Retrieve the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square.

        Args:
            value (int): The size of the square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        if value < 0:
            raise ValueError

        self.__size = value

    @property
    def area(self):
        """Compute the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    @property
    def position(self):
        """
        Position the square

        Returns:
        (str): The positioned square
        """
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position of the square."""
        if not isinstance(value, tuple) or len(value) != 2 or \
           not isinstance(value[0], int) or not isinstance(value[1], int) or \
           value[0] < 0 or value[1] < 0:
               raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        """Print the square with the character '#'."""
        if self.__size == 0:
            print()

        else:
            for i in range(self.__position[1]):
                print()
            for i in range (self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
