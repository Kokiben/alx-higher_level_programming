#!/usr/bin/python3
"""Collect all parameters into a Python list and store them in a file."""
import sys

if __name__ == "__main__":
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = \
        __import__('6-load_from_json_file').load_from_json_file

    try:
        ite = load_from_json_file("add_item.json")
    except FileNotFoundError:
        ite = []
    ite.extend(sys.argv[1:])
    save_to_json_file(ite, "add_item.json")
