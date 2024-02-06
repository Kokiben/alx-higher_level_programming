#!/usr/bin/python3
"""Define a function to serialize a  Python class to JSON."""


def class_to_json(obj):
    """Return the dictionary represntation of a basic data structure."""
    return obj.__dict__
