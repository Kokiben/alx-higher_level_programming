#!/usr/bin/python3
"""Defines a class Student."""


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
            result = {}
            for key, value in self.__dict__.items():
                if key in attrs:
                    result[key] = value
            return result

    def reload_from_json(self, json):
        """Exchange all characteristics of the Student.

        Args:
            json (dict): A dictionary containing key/value pairs
            to substitute student characteristics.
        """
        for key, value in json.items():
            setattr(self, key, value)
