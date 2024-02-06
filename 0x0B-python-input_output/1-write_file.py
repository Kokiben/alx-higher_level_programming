#!/usr/bin/python3
"""Defines a function creating a text file and storing a string inside."""


def write_file(filename="", text=""):
    """creat a text file containing a string .

    Args:
        filename (str): The file to write.
        text (str): Write to the file.
    Returns:
        The number of characters written.
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
