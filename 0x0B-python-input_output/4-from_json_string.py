#!/usr/bin/python3
"""Defines a function for parsing a JSON string to into an object."""
import json


def from_json_string(my_str):
    """parses a JSON string into  an object.

        Return an object represented by a JSON string."""

    return json.loads(my_str)
