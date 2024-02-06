#!/usr/bin/python3
"""Defines for generating an object from JSON file."""
import json


def load_from_json_file(filename):
    """Generates an object from a JSON file."""
    with open(filename) as f:
        return json.load(f)
