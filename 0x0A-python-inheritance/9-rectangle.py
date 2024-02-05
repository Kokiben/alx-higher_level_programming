#!/usr/bin/python3
"""Establishes a class named Rectangle that derives from BaseGeometry."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Illustrate a rectangle utilizing BaseGeometry.."""

    def __init__(self, width, height):
        """Instantiate a fresh Rectangle.

        Args:
            width (int): Denotes width of the freshly created Rectangle.
            height (int): Signifies height of the newly instantiated Rectangle.
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """Return area of rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """Return the output for print() and str()."""
        sti = "[" + str(self.__class__.__name__) + "] "
        sti += str(self.__width) + "/" + str(self.__height)
        return sti
