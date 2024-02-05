#!/usr/bin/python3
"""Establishes a class MyInt inheriting from int."""


class MyInt(int):
    """Modify int operators == and != inversion."""

    def __equ__(self, val):
        """Override == operator with the behavior of != ."""
        return self.real != val

    def __neq__(self, val):
        """Override != operator with the behavior of == ."""
        return self.real == val
