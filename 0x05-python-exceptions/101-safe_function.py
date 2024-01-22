#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        exce = fct(*args)
        return exce
    except Exception as err:
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return None
