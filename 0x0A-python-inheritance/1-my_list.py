#!/usr/bin/python3
"""Defines a class named MyList that inherits from a list."""


class MyList(list):
    """Print sorted display for the standard list class."""

    def print_sorted(self):
        """Display a list in ascending sorted order."""
        print(sorted(self))
