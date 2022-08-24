#!/usr/bin/python3
for i in range(0, 10):
    for j in range(1, 10):
        if i < j:
            if (i + j >= 2) and (int(str(i) + str(j)) <= 89):
                print(end=", ")
            print("{}{}".format(i, j), end="")
print()
