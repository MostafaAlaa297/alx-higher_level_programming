#!/usr/bin/python3
"""
===============
file I/O module
===============
"""
def to_json_string(my_obj):
    import json
    """
    return JSON of an object
    """
    return json.dumps(my_obj)
