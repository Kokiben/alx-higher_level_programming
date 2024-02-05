#!/usr/bin/python3
"""Define a function for looking up object attribute."""


def lookup(obj):
    """Return a list of attributes accessible for an obj."""
    return (dir(obj))
