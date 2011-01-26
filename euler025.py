#!/usr/bin/python

from math import ceil, log10

PHI = 1.6180339887
x = 0
i = 0
while x < 1000:
    i += 1
    x = ceil(i * log10(PHI) - log10(5) / 2)
    print(i, x)

print(i)
