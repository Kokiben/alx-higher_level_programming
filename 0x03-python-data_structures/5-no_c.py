#!/usr/bin/python3
def no_c(my_string):
    res = ""
    a = 0
    while a < len(my_string):
        if my_string[a] not in ('c', 'C'):
            res += my_string[a]
        a += 1
    return (res)
