#!/usr/bin/python3
"""
Status Module
"""
if __name__ == "__main__":
    import requests
    import sys
    url = sys.argv[1]

    try:
        response = requests.get(url)
        print(response.text)
    except requests.exceptions.HTTPError as e:
        print("Error code:", e.code)
