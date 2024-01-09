#!/usr/bin/python3
"""
=================
file I/O module
=================
"""

def read_file(filename=""):
    """
    reading a file in utf-8
    """
    with open(filename, "r", encoding="utf-8") as file:
        print(file.read())
