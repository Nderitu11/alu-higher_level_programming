#!/usr/bin/python3
"""Fetches https://alu-intranet.hbtn.io/status and displays the body."""
import urllib.request


if __name__ == "__main__":
    with urllib.request.urlopen("https://alu-intranet.hbtn.io/status") as resp:
        body = resp.read()
        print("Body response:")
        print("\ttype: {}".format(type(body)))
        print("\tcontent: {}".format(body))
        print("\tutf8 content: {}".format(body.decode("utf-8")))
