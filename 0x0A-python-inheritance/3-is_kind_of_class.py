#!/usr/bin/python3
"""
Defines a class and a function for verifying inheritance.
"""


def is_kind_of_class(obj, a_class):
    """
    Verify if the object obj is an instance or inherited instance of the specified class a_class,
    returning True if it is,
    and False otherwise.
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
