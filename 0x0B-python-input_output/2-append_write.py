#!/usr/bin/python3
"""
===============
file I/O module
===============
"""
def append_write(filename="", text=""):
    """
    append to file
    """
    with open(filename, "a", encoding="utf-8") as file:
        return file.write(text)
