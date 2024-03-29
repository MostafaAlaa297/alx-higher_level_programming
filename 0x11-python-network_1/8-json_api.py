#!/usr/bin/python3
"""
Status Module
"""
if __name__ == "__main__":
    import requests
    import sys

    if len(sys.argv) == 1:
        q = ""
    else:
        q = sys.argv[1]
    url = 'https://alx-intranet.hbtn.io/status'
    data = {'q': q}
    res = requests.post(url, data = data)

    try:
        data = respoonse.json()
        if data:
            print("[{}] {}".format(data.get('id'), data.get('name')))
        else:
            print("No result")
     except ValueError:
        print("Not a valid JSON")
