#!/usr/bin/python3
#  Prints the number of and the list of its arguments
if __name__ == "__main__":
    import sys

    a = sys.argv
    s = len(a) - 1

    if s > 1:
        print("{} arguments:".format(s))
        for n in range(1, s + 1):
            print("{}: {}".format(n, a[n]))

    elif s == 0:
        print("{} arguments.".format(s))

    else:
        print("{} argument:".format(s))
        print("{}: {}".format(s, a[1]))
