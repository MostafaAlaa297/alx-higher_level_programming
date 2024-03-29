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

    url = 'http://0.0.0.0:5000/search_user'
    data = {'q': q}
    res = requests.post(url, data=data)

    try:
        data = res.json()
        if data:
            print("[{}] {}".format(data.get('id'), data.get('name')))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
