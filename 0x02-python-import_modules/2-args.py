#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    length = len(sys.argv)
    if length == 0:
        print("0 arguments.")
    else:
        if length == 1:
            print("{} argument:".format(length))
        elif length >= 2:
            print("{} arguments:".format(length))
        for num in range(length):
            number = 1 + num
            print("{:d}: {:s}".format(number, sys.argv[num]))
