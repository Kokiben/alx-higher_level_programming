#!/usr/bin/python3
def add_arg(argv):
    a = len(argv) - 1
    if a == 0:
        print("{:d}".format(a))
        return
    else:
        m = 1
        add = 0
        while m <= a:
            add += int(argv[m])
            m += 1
        print("{:d}".format(add))


if __name__ == "__main__":
    import sys
    add_arg(sys.argv)
