#!/usr/bin/pthon3
"""
Is same class
"""
def is_same_class(obj, a_class):
    """
    Returns True if the object ddddis exactly an instance of the specified class;
    otherwise, False.
    """
    return type(obj) is a_class
