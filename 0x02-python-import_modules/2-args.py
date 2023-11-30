#!/usr/bin/python3
def print_args(argv):
    n = len(argv) - 1
    if n == 0:
        print("0 arguments")
    else:
        if n == 1:
            print("1 argument:")
        else:
            print("{:d} arguments:".format(n))
        for i, arg in enumerate(argv[1:], start=1):
            print("{:d}: {:s}".format(i, arg))

if __name__ == "__main__":
    import sys
    print_args(sys.argv)
