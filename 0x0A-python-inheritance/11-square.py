#!/usr/bin/python3
"""Establishes a Square derivative of Rectangle."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Illustrate a square."""

    def __init__(self, size):
        """Instantiate a fresh square.

        Args:
            size (int): Denotes the size of the newly created square..
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
