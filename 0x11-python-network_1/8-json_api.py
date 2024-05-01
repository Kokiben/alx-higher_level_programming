#!/usr/bin/python3
"""Print a Python script that takes in a letter and sends a POST """
import requests
import sys


if __name__ == "__main__":
    lttr_vrbl = "" if len(sys.argv) == 1 else sys.argv[1]
    narg = {"q": lttr_vrbl}

    rqt = requests.post("http://0.0.0.0:5000/search_user", data=narg)
    try:
        rps = rqt.json()
        if rps == {}:
            print("No result")
        else:
            print("[{}] {}".format(rps.get("id"), rps.get("name")))
    except ValueError:
        print("Not a valid JSON")
