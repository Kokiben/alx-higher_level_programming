#!/usr/bin/python3
""" Sends a request to  URL and displays body of response. """
import requests
import sys

if __name__ == "__main__":
    urll = sys.argv[1]
    rq = requests.get(urll)
    if (rq.status_code >= 400):
        print(f"Error code: {req.status_code}")
        exit()
    print(rq.text)
