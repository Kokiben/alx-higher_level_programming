#!/usr/bin/python3
def uppercase(str):
    for c in str:
        if 'a' <= c <= 'z':
            min = ord('a') - ord('A')
        else:
            min = 0
        print("{:s}".format(chr(ord(c) - min)), end="")
    print("")
