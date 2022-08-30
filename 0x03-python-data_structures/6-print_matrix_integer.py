#!/usr/bin/python3
x = 3
y = 3
matrix = [[(i+1)+(j*x) for i in range(x)] for j in range(y)]
for row in matrix:
    print(' '.join(map(str, row)))
