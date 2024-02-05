#!/usr/bin/python3
"""Establishes a class MyInt inheriting from int."""


class MyInt(int):
    """Modify int operators == and != inversion."""

    def __eq__(self, value):
        """Override == opeartor with != behavior."""
        return self.real != value

    def __ne__(self, value):
        """Override != operator with == behavior."""
        return self.real == value
