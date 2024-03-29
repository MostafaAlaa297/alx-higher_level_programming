#!/usr/bin/python3
"""
Github auth
"""
if __name__ == "__main__":
    import requests
    import sys

    username = sys.argv[1]
    password = sys.argv[2]

    res = requests.get(
            "https://api.github.com/user",
            auth=(username, password)
            )
    if res.status_code == 200:
        data = res.json()
        print(data.get('id'))
    else:
        print(None)
