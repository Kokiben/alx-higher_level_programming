#!/usr/bin/python3
"""Defines a function reads a text file"""


def read_file(filename=""):
    """ function """
    with open(filename, encoding="utf-8") as f:
        read_op = f.read()
        print(read_op, end="")
