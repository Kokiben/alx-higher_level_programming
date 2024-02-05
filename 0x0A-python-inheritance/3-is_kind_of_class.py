#!/usr/bin/python3
"""
Defines a class and a function for verifying inheritance.
"""


def is_kind_of_class(obj, a_class):
    """
    Create a function that determines whether an object is
    an instance of the specified class or an inherited class.
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
