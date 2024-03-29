#!/usr/bin/python3
"""
Status Module
"""
if __name__ == "__main__":
    import urllib.parse
    import urllib.request
    import sys
    url = sys.argv[1]

    try:
        with urllib.request.urlopen(url) as response:
            print(response.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
