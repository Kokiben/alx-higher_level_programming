#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list is not None:
        for a in range(len(my_list)):
            print("{:d}".format(my_list[::-1][a]))
