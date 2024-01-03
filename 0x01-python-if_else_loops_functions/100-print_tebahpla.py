#!/usr/bin/python3
for c in range(25, -1, -2):
    print("{:s}{:s}".format(chr(c + ord("a")),
          chr(c - 1 + ord("a")).upper()), end="")
