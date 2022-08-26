#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    length = len(sys.argv) - 1
    if length == 0:
        print("0 arguments.")
    else:
        if length == 1:
            print("1 argument:")
        else:
            print("{} arguments:".format(length))
        for num in range(length):
            number = 1 + num
            print("{:d}: {:s}".format(number, sys.argv[num]))
