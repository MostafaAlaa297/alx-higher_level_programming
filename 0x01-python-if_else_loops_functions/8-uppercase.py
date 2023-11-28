#!/usr/bin/python3
def uppercase(c):
    for char in c:
        print("{:c}".format(ord(char) - 32) if ord(char) >= 97 and ord(char) <= 122 else char, end="")
    print()
