#!/usr/bin/python3
"""Defines for saving  an Object to a text file using a JSON serialization."""
import json


def save_to_json_file(my_obj, filename):
    """Saves an Object to a text file, employing a JSON serialization."""

    with open(filename, 'w') as f:
        json.dump(my_obj, f)
