#!/usr/bin/python3
import urllib.request
import sys
"""
Status Module
"""
if __name__ == "__main__":
    url = sys.argv[1]

with urllib.request.urlopen(url) as response:
    headers = response.headers
    x_req_id = headers.get("X-Request-Id")
    print(x_req_id)
