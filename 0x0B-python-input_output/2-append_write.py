#!/usr/bin/python3
"""Defines a function appends a string at the end of a text file ."""


def append_write(filename="", text=""):
    """Appends a string to the end of another string wihtin a text file.

    Args:
        filename (str): File name to append to.
        text (str): String to append onto the file.
    Returns:
        The number of characters added.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
