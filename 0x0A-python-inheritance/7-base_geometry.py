#!/usr/bin/python3
"""Establishes a blank class called BaseGeometry."""


class BaseGeometry:
    """Illustrate fundamental geometric principles."""

    def area(self):
        """Not presently implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Verify a parameter as an integer.

        Args:
            name (str): Denotes the parameter name.
            value (int): Represents the parameter under scrutiny.
        Raises:
            TypeError: Raised if value is not an integer.
            ValueError: Raised if value is less than or equal to 0.
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
