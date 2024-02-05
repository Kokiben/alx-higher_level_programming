#!/usr/bin/python3
"""
Create a function for checking inheritance in a defined class.
"""


def inherits_from(obj, a_class):
    """
    Construct a function that checks if an object is an instance of a class
    that inherited (either directly or through intermediate classes) from the specified class.
    """
    if issubclass(type(obj), a_class) and type(obj) is not a_class:
        return True
    else:
        return False
