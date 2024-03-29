#!/usr/bin/python3
"""
Status Module
"""
if __name__ == "__main__":
    import requests
    url = 'https://alx-intranet.hbtn.io/status'
    res = requests.get(url)

    print("Body response:")
    print("\t- type:", type(res.text))
    print("\t- content:", res.text)
