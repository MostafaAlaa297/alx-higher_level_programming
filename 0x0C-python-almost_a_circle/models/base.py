#!/usr/bin/python3

"""
===========
base module
===========
"""
import json

class Base:
    """The Base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a new instance of the Base class."""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)
    
    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string representation json_string."""
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)
    
    @classmethod
    def save_to_file(cls, list_objs):
        if list_objs is None:
            list_objs = []
        
        json_string = cls.to_json_string([obj.to_dictionary() for obj in list_objs])

        with open("{}.json".format(cls.__name__), "w") as file:
            file.write(json_string)

    @classmethod
    def create(cls, **dictionary):
        """create dummy instance and set it the return it"""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls__name__ == "Square":
            dummy = cls(1)
        else:
            return None
        dummy.update(**dictionary)
        return dummy
        
