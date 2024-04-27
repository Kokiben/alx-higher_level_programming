#!/usr/bin/python3
"""Call https://alx-intranet.hbtn.io/status."""
import urllib.request


if __name__ == "__main__":
    request_id = urllib.request.Request("https://alx-intranet.hbtn.io/status")
    with urllib.request.urlopen(request_id) as response:
        body = response.read().decode('utf-8')
        print("- Body response:")
        print("\t- type:", type(body))
        print("\t- content:", body)
        print("\t- utf8 content:", body)
