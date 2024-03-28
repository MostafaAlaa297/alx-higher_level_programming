#!/usr/bin/python3
import urllib.parse
import urllib.request
import sys
"""
Status Module
"""
if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    data = urllib.parse.urlendode({'email': email}).encode('utf-8')
    req = urllinb.Request(url, data)

    with urllib.request.urlopen(url) as response:
        body = response.read().decode('utf-8')
        print(body)
