#!/usr/bin/python3
"""Call https://alx-intranet.hbtn.io/status."""
import urllib.request

urll = "https://alx-intranet.hbtn.io/status"

with urllib.request.urlopen(url) as response:
    body = response.read().decode('utf-8')

print("- Body response:")
print("\t- type:", type(body))
print("\t- content:", body)
