#!/usr/bin/python3
"""
===============
file I/O module
===============
"""
import json
def load_from_json_file(filename):
    """
    creat obj from json  file
    """

    with open(filename, mode="r", encoding="utf-8") as file:
        return json.load(file)
