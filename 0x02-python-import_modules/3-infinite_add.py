#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    res = 0
    for i, arg in enumerate(argv[1:], start=1):
        res += int(arg)
    print("{}".format(res))
