#!/usr/bin/python3
""" Sends a request to  URL and displays body of response. """
import requests
import sys

if __name__ == "__main__":
    urll = sys.argv[1]
    rqt = requests.get(urll)
    if (rqt.status_code >= 400):
        print(f"Error code: {rqt.status_code}")
        exit()
    print(rqt.text)
