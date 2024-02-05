#!/usr/bin/python3
"""Establishes a function that appends attributes to objects."""


def add_attribute(obj, a, va):
    """Incorporate a new attribute into an object if possible.

    Args:
        obj (any): The object for attribute addition.
        a (str):The attribute name to incorporate into obj.
        va (any): The value assigned to the attribute.
    Raises:
        TypeError: Raised if it's not possible to add the attribute..
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, a, va)
