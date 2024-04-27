#!/usr/bin/python3
""" Sends a request to URL and displays value of variable X-Request-Id """
import requests
import sys

if __name__ == "__main__":
    urll = sys.argv[1]
    rq = requests.get(urll)
    print(rq.headers.get("X-Request-Id"))
