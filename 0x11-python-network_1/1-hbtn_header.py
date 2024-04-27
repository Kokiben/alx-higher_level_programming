#!/usr/bin/python3
""" Displays value of X-Request-Id variable found in header """
import urllib.request
import sys


if __name__ == "__main__":
    url = sys.argv[1]

    with urllib.request.urlopen(url) as response:
        request_id = response.getheader('X-Request-Id')
        print("X-Request-Id:", request_id)

