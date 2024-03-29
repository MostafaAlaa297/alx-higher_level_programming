#!/usr/bin/python3
"""
Status Module
"""
if __name__ == "__main__":
    import requests
    import sys
    url = sys.argv[1]

    response = requests.get(url)
    headers = response.headers['X-Request-Id']
    print(headers)
