#!/usr/bin/python3

"""Class definition for a Square."""


class Square:
    """A simple represention of a square."""

    def __init__(self, side_leng = 0):
        """Initialize a new Square with a specified side leng.

        Args:
            side_leng (int): The side leng of the new square.
        """
        if type(side_leng) is not int:
            raise TypeError("side_leng must be an integer")
        if side_leng < 0:
            raise ValueError("side_leng must be >= 0")
        self.__size = side_leng
