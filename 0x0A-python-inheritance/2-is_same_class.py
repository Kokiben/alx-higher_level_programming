#!/usr/bin/python3
"""
Defines a function for checking object class.
"""


def is_same_class(obj, a_class):
    """
    Verify if an entity is precisely an instance of a specified class.
    """
    if type(obj) is a_class:
        return True
    else:
        return False
