#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    a = sys.argv
    s = len(a) - 1

    if s > 1:
        print("{} arguments:".format(s))
        for m in range(1, s + 1):
            print("{}: {}".format(m, a[m]))

    elif s == 0:
        print("{} arguments.".format(s))

    else:
        print("{} argument:".format(s))
        print("{}: {}".format(s, a[1]))
