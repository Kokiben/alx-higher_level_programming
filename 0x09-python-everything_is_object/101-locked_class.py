#!/usr/bin/python3
"""Introduces a locked class."""


class LockedClass:
    """
    Restrict instantiation of new attributes in RestrictedClass
    to only allow attributes named 'first_name'.
    """

    __slots__ = ["first_name"]
