#!/usr/bin/python3
"""
My add_integer module
"""
def add_integer(a, b=98):
    """ method for adding two numbers """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    elif not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a + b)
