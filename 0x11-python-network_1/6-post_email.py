#!/usr/bin/python3
"""Sends a POST request to the passed URL with the email as a parameter"""
import requests
import sys


if __name__ == "__main__":
    urll = sys.argv[1]# Get the URL from the command-line argument
    ema = {"email": sys.argv[2]}
    rq = requests.post(urll, data=ema)
    print(rq.text)
