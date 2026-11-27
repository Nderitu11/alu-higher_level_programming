#!/usr/bin/python3
"""Fetches https://alu-intranet.hbtn.io/status using urllib."""
import urllib.request


if __name__ == "__main__":
    url = "https://alu-intranet.hbtn.io/status"
    with urllib.request.urlopen(url) as response:
        body = response.read()
        print("Body response:")
        print("\ttype: {}".format(type(body)))
        print("\tcontent: {}".format(body))
        print("\tutf8 content: {}".format(body.decode("utf-8")))
