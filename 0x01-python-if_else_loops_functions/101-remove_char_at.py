#!/usr/bin/python3
def remove_char_at(str, n):
    w = ""
    for index, c in enumerate(str):
        if index != n:
            w = w + c
    return (w)
