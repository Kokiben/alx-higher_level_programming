#!/usr/bin/python3
""" Sends a request to URL and displays body of response """
import urllib.request
import sys
import urllib.error


if __name__ == "__main__":
    try:
        urll = sys.argv[1] # Get the URL from the command-line argument
        with urllib.request.urlopen(urll) as rps: # Open the URL and read
            print(rps.read().decode('utf-8'))
    except urllib.error.HTTPError as err: # Handle HTTP errors
        print(f"Error code: {err.code}"
