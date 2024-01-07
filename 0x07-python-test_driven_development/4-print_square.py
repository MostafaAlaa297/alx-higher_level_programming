#!/usr/bin/python3
"""
print_square module
"""
def print_square(size):
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    square = ""
    for _ in range(size):
            square += "#" * size + "\n"
    print(square, end="")
