#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_d = str(number)
last_d = last_d[-1]
last_d_int = int(last_d)
if last_d_int > 5:
    print(f"Last digit of {number} is {last_d} and is greater than 5")
elif last_d_int == 0:
    print(f"Last digit of {number} is {last_d} and is {last_d}")
else:
    print(f"Last digit of {number} is {last_d} and is less than 6 and not 0")
