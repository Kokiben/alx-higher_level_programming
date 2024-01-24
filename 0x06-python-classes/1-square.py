#!/usr/bin/python3

"""Class definition for a Square."""


class Square:
    """A simple represention of a square."""

    def __init__(self, side_leng):
        """Initialize a new Square with a specified side leng.

        Args:
            side_leng (int): The side leng of the new square.
        """
        self.__size = side_leng
