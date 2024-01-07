#!/usr/bin/python3

"""
This is the "Rectangle"  module.

This module provides a simple Rectangle class with attribute width and height.
Default values of both attributes are 0.
"""

class Rectangle:
    """
    Defines a rectangle.
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Initializes a new rectangle instance.
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        
        self.__height = value

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        return 2 * (self.__width + self.__height) if self.__width and self.height else 0

    def __str__(self):
        if not self.__width or not self.__height:
            return ""

        if isinstance(self.print_symbol, list):
            return "\n".join("".join(str(symbol) for symbol in self.print_symbol) for _ in range(self.__height))
        else:
            return "\n".join(str(self.print_symbol) * self.__width for _ in range(self.__height))

    def __repr__(self):
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        return rect_1 if rect_1.area() >= rect_2.area() else rect_2
    
    @classmethod
    def square(cls, size=0):
        return cls(size, size)
