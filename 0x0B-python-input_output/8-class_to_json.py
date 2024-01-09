#!/usr/bin/python3
"""
returns the dictionary description with simple data structure
(list, dictionary, string, integer and boolean)
for JSON serialization of an object
"""
def class_to_json(obj):
    """Converts a class instance to a JSON-serializable dictionary."""
    json_dict = {}

    attributes = obj.__dict__

    for key, value in attributes.items():
        if "__dict__" in dir(value):
            json_dict[key] = class_to_json(value)
        else:
            json_dict[key] = value

    return json_dict
