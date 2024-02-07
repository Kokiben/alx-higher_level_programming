#!/usr/bin/python3
"""Class Definition for Student."""


class Student:
    """A simple represention of a student."""

    def __init__(self, first_name, last_name, age):
        """Initialize a new Student.

        Args:
            first_name (str): Name first of student.
            last_name (str): Name last of student.
            age (int): Age of student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Provide the dictionary depiction of the Student."""
        if attrs is None:
            return self.__dict__
        else:
            sult = {}
            for ky, val in self.__dict__.items():
                if ky in attrs:
                    sult[ky] = val
            return sult
