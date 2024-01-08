#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    s1 = tuple_a + (0, 0)
    s2 = tuple_b + (0, 0)
    return s1[0] + s2[0], s1[1] + s2[1]
