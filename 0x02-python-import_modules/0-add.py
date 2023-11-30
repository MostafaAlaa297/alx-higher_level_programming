#!/usr/bin/python3
if __name__ == "__main__":
    a, b = 1, 2
    add_0 = __import__("add_0")
    print("{:d} + {:d} = {:d}".format(a, b, add_0.add(a, b)))
