#!/usr/bin/python3
"""Crafts a function to sum up integers, ensuring type consistency by converting inputs when needed."""


def add_integer(a, b=98):
    """Return sum of int a and b.

    Before performing addition, the function converts float arguments to integers.

    Raises:
    """
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
