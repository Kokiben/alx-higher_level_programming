#!/usr/bin/python3
""" Displays value of X-Request-Id variable found in header """
import urllib.request
import sys


if __name__ == "__main__":
    url = sys.argv[1]

    request_id = requests.get(url)

    print(request_id.headers.get("X-Request-Id"))
