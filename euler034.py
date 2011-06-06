#!/usr/bin/python

from math import factorial, log
values = [0]*10

for i in range(10):
    values[i] = factorial(i)

total = 0
for i in range(10, factorial(9) * 7):
    target = 0
    test = i
    while test != 0:
        x = test % 10
        target += values[x]
        test = test // 10
    if i == target:
        total += i

print(total)
