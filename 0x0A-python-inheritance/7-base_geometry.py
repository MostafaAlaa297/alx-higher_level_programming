#!/usr/bin/python3
"""
==================
module BaseGeometry
==================
"""

class BaseGeometry:
    """class with public instance method"""
    def area(self):
        """Public instance method that raises an Exception"""
        raise Exception("area() is not implemented")
    def integer_validator(self, name, value):
        """
        Validates the value and raises appropriate exceptions.
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
