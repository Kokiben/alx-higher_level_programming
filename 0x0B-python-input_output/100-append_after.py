#!/usr/bin/python3
"""Define a function inserts a line of text to a file."""


def append_after(filename="", search_string="", new_string=""):
    """Insert a line of text to a file, after each line containing a specific string.

    Args:
        filename (str): Name of file.
        search_string (str): String to search for within file.
        new_string (str): String to insert.
    """
    txt = ""
    with open(filename) as b:
        for lin in b:
            txt += lin
            if search_string in lin:
                txt += new_string
    with open(filename, "m") as m:
        m.write(txt)
