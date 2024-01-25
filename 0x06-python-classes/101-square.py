#!/usr/bin/python3
"""Class definition for a Square."""


class Square:
    """A simple represention of a square."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a new Square with a specified size"""
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """Retrieve method to get size of square."""
        return self.__size

    @size.setter
    def size(self, val):
        """Assigner method to define size of square."""
        if not isinstance(val, int):
            raise TypeError("size must be an integer")
        elif val < 0:
            raise ValueError("size must be >= 0")
        self.__size = val

    @property
    def position(self):
        """Retrieve method to get position."""
        return self.__position

    @position.setter
    def position(self, val):
        """Assigner method to define position."""
        if (
            not isinstance(val, tuple)
            or len(val) != 2
            or not all(isinstance(n, int) for n in val)
            or not all(n >= 0 for n in val)
        ):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = val

    def area(self):
        """Compute and return the square's area."""
        return self.__size * self.__size

    def __str__(self):
        """Return a string depicting the square using '#'."""
        if self.__size == 0:
            return ""

        res = ""
        for _ in range(self.__position[1]):
            res += "\n"
        for _ in range(self.__size):
            res += " " * self.__position[0] + "#" * self.__size + "\n"

        return result[:-1]
