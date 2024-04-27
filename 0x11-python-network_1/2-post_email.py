#!/usr/bin/python3
""" POST request to the passed URL with the email as a parameter """
import urllib.request
import urllib.parse
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    ema = {"email": sys.argv[2]}
    # Encode the email parameter
    dat = urllib.parse.urlencode(ema).encode("ascii")
    # Create a POST request
    req = urllib.request.Request(url, dat)
    # Send the request and read the response
    with urllib.request.urlopen(req) as response:
        print(response.read().decode("utf-8"))
