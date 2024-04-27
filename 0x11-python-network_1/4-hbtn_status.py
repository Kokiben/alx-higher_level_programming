#!/usr/bin/python3
"""Call https://alx-intranet.hbtn.io/status."""
import requests


if __name__ == "__main__":
    rq = requests.get("https://alx-intranet.hbtn.io/status")
    print("Body response:")
    print("\t- type:", type(rq.text))
    print("\t- content:", (rq.text))
