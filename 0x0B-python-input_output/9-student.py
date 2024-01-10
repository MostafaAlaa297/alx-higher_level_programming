#!/usr/bin/python3
"""
===============
file I/O module
===============
"""
class Student:
    """
    Student class
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Converts a class instance to a JSON-serializable dictionary.
        """
        student_dict = {}

        attributes = self.__dict__

        for key, value in attributes.items():
            if '__dict__' in dir(value):
                student_dict[key] = to_json(value)
            else:
                student_dict[key] = value
        return student_dict
