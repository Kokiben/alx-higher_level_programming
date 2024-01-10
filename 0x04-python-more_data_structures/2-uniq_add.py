#!/usr/bin/python3
def uniq_add(my_list=[]):
    m = 0
    for n in set(my_list):
        m += n
    return m
