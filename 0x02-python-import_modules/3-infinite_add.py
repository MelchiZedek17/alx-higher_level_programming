#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    total = 0
    for number in argv:
        if type(number) == int or type(number) == float:
            total += number
    print("{}".format(total))
