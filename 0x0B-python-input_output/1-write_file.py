#!/usr/bin/python3
"""
===============
file I/O module
==============
"""
def write_file(filename="", text=""):
    """
    write to file
    """
    with open(filename, "w", encoding="utf-8") as file:
        return file.write(text)