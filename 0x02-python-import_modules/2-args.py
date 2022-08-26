#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    num_args = len(sys.argv) - 1
    if num_args == 0:
        print("0 arguments.")
    else:
        if num_args == 1:
            print("{} argument:".format(num_args))
        else:
            print("{} arguments:".format(num_args))
    for num in range(num_args):
        number = num + 1
        print("{:d}: {:s}".format(number, sys.argv[number]))
