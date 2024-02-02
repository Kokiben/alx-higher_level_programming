#!/usr/bin/python3
"""
Crafts a function to sum up integers, ensuring type consistency by converting inputs when needed..

The 0-add_integer module.
"""


def add_integer(a, b):
    """Return sum of int a and b."""
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)
    return a + b
