#!/usr/bin/python3
import sys
if __name__ == "__main__":
    arg_length = len(sys.argv)
    if arg_length == 0:
        print("0 arguments.")
    else:
        print("{} arguments:".format(arg_length))
        for num in range(arg_length):
            numbering = 1 + num
            print("{}: {}".format(numbering, sys.argv[num]))
