#!/usr/bin/python3

""" Class definition for a Square."""


class Square:
    """A simple represention of a square."""

    def __init__(self, size=0):
        """Initialize a new square with a specified size leng.

        Args:
            size_leng (int): The size leng of the new square.
        """
        if not isinstance(size_leng, int):
            raise TypeError("size leng must be an integer")
        elif size_leng < 0:
            raise ValueError("size leng must be >= 0")
        self.__size = size_leng

    def area(self):
        """Return current area square."""
        return (self.__size * self.__size)
