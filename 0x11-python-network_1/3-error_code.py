#!/usr/bin/python3
""" module doc """
import urllib.request
import sys
import urllib.error

if __name__ == "__main__":
    try:
        urll = sys.argv[1] # Get the URL from the command-line argument
        # Open the URL and read
        with urllib.request.urlopen(urll) as rps:
            print(rps.read().decode('utf-8'))
    except urllib.error.HTTPError as err:
    # Handle HTTP errors
        print(f"Error code: {err.code}"
        # Print the HTTP status code of the error
