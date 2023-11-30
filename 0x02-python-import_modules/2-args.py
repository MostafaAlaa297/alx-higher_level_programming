#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    length = len(argv) - 1
    plural = "s" if length != 1 else ""
    period = "." if length == 0 else ":"

    print("{:d} argument{:s}{:s}".format(length, plural, period))

    for i, arg in enumerate(argv[1:]):
        print("{:d}: {:s}".format(i, arg))
