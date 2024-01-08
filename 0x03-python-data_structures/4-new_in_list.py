#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    n = list(my_list)
    if idx < 0 or idx > len(n) - 1:
        return (n)
    n[idx] = element
    return (n)
