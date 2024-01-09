#!/usr/bin/python3
"""
===============
file I/O module
===============
"""
import json
def save_to_json_file(my_obj, filename):
    """
    write json to a file
    """

    with open(filename, mode="w", encoding="utf-8") as file:
        json.dump(my_obj, file)
