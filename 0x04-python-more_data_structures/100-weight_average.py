#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    a = 0
    d = 0
    for tuple in my_list:
        a = a + tuple[0] * tuple[1]
        d = d + tuple[1]

    return a / d
