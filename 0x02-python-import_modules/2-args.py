#!/usr/bin/python3
from sys import argv
length = len(argv)
if length - 1 == 0:
    print("0 arguments.")
elif length - 1 == 1:
    print("1 argument: ".format(len(argv) - 1))
    print("1: {}".format(argv[1]))
elif length > 1:
    print("{} arguments.".format(length - 1))
    for i in range(1, length):
        print("{}: {}".format(i, argv[i]))
