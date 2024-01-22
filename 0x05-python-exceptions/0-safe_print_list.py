#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    a = 0
    for a in range(x):
        try:
            print("{}".format(my_list[a]), end="")
        except IndexError:
            break
        else:
            a += 1
    print("")
    return (a)
