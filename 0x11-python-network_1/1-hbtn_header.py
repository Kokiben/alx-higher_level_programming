#!/usr/bin/python3
""" Displays value of X-Request-Id variable found in header """
import urllib.request
import sys


if __name__ == "__main__":
    url = sys.argv[1]

    request_id = urllib.request.Request(url)
    with urllib.request.urlopen(request_id) as response:
        print(dict(response.headers).get("X-Request-Id"))
