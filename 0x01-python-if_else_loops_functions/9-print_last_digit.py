#!/usr/bin/python3
def print_last_digit(number):
    num_str = str(number)
    last_d = int(num_str[-1])
    print(f"{last_d}", end="")
    return last_d
