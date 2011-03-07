#!/usr/bin/python

from functools import reduce
from math import sqrt

pan_set = set()

for i in range(1000, 9999):
    for j in range(2, int(sqrt(i)) + 1):
        if j * (i // j) == i:
            if len(set(str(j) + str(i // j) + str(i)) - set('0')) == 9:
                pan_set.add(i)

print(sum(pan_set))
