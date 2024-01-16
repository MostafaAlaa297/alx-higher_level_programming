#!/usr/bin/python3

"""
===========
base module
===========
"""
import json

class Base:
    """
    the base class
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialization of the base module"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """convert list to json string"""
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """convert json string to dictionary"""
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    def to_dictionary(self):
        """Return the dictionary representation of the instance."""
        return {"id": self.id}

    def update(self, *args, **kwargs):
        """Update the attributes of the instance."""
        if args:
            if len(args) > 0:
                self.id = args[0]
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    @classmethod
    def save_to_file(cls, list_objs):
        """save to file"""
        if list_objs is None:
            list_objs = []

        json_string = cls.to_json_string([obj.to_dictionary() for obj in list_objs])

        with open("{}.json".format(cls.__name__), "w") as file:
            file.write(json_string)

    @classmethod
    def create(cls, **dictionary):
        """create instances from a dictionary"""
        dummy = cls(1)  # Assuming default values, update as needed
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """create instance list from json file"""
        filename = "{}.json".format(cls.__name__)

        try:
            with open("{}.json".format(cls.__name__), "r") as file:
                json_string = file.read()
        except FileNotFoundError:
            return []

        obj_list = cls.from_json_string(json_string)
        instance_list = [cls.create(**obj) for obj in obj_list]

        return instance_list
