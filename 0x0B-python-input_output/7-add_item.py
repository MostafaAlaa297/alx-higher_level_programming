#!/usr/bin/python3
"""
===============
file I/O module
===============
"""
import sys
from os import path
from json import dump, load
from importlib import import_module

save_to_json_file = import_module('5-save_to_json_file').save_to_json_file
load_from_json_file = import_module('6-load_from_json_file').load_from_json_file

if __name__ == "__main__":
    filename = "add_item.json"

    if path.exists(filename):
        my_list = load_from_json_file(filename)
    else:
        my_list = []

    my_list.extend(sys.argv[1:])

    save_to_json_file(my_list, filename)
