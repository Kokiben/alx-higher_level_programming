#!/usr/bin/python3
"""Call https://alx-intranet.hbtn.io/status."""
import urllib.request


if __name__ == "__main__":
    rq = urllib.request.Request("https://alx-intranet.hbtn.io/status")
    with urllib.request.urlopen(rq) as rps:
        body = rps.read().decode('utf-8')
        print("- Body response:")
        print("\t- type:", type(body))
        print("\t- content:", body)
        print("\t- utf8 content:", body)
