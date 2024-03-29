#!/usr/bin/python3
import urllib.parse
import urllib.request
import sys
"""
Status Module
"""
if __name__ == "__main__":
    url = sys.argv[1]
    req = urllib.request.Request(url)

    try:
        urllib.request.urlopen(req)
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
