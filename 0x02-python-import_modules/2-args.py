#!/usr/bin/python3
import sys
length = len(sys.argv) - 1
if length == 0:
    print("0 arguments.")
elif length == 1:
    print("1 argument: ".format(len(sys.argv) - 1))
    print("1: {}".format(sys.argv[1]))
elif length > 1:
    print("{} arguments.".format(len(sys.argv) - 1))
    for i in range(1, length + 1):
        print("{}: {}".format(i, sys.argv[i]))
