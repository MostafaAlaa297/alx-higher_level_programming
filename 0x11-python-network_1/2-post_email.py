#!/usr/bin/python3
"""
Status Module
"""
if __name__ == "__main__":
    import urllib.parse
    import urllib.request
    import sys

    url = sys.argv[1]
    email = sys.argv[2]
    
    payload = {'email': email}
    payload = urllib.parse.urlencode(payload)
    payload = payload.encode('ascii')
    req = urllib.request.Request(url, payload)

    with urllib.request.urlopen(url, payload) as response:
        print("Your email is:", email)
        body = response.read().decode('utf-8')
        print(body)
