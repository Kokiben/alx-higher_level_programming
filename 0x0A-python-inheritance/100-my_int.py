#!/usr/bin/python3
"""Establishes a class MyInt inheriting from int."""


class MyInt(int):
    """Modify int operators == and != inversion."""

    def __eq__(self, val):
        """Override == operator with the behavior of != ."""
        return self.real != val

    def __ne__(self, val):
        """Override != operator with the behavior of == ."""
        return self.real == val
