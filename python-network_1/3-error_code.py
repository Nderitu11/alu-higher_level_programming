#!/usr/bin/python3
"""Displays a URL response body and handles HTTP errors with urllib."""
import sys
import urllib.error
import urllib.request


if __name__ == "__main__":
    try:
        with urllib.request.urlopen(sys.argv[1]) as response:
            print(response.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
