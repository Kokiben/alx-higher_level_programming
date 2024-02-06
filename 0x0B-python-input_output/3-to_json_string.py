#!/usr/bin/python3
"""Establishes a function to convert a string to JSON."""
import json


def to_json_string(my_obj):
    """Return the JSON format of a string entity."""
    return json.dumps(my_obj)
