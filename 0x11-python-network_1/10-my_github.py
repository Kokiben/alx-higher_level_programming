#!/usr/bin/python3
"""Print a Python script that takes your GitHub credentials"""
import sys
from requests.auth import HTTPBasicAuth
import requests


if __name__ == "__main__":
    ah = HTTPBasicAuth(sys.argv[1], sys.argv[2])
    rqt = requests.get("https://api.github.com/user", auth=ah)
    print(rqt.json().get("id"))
