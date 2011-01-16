#!/usr/bin/python

"""
First attempt to resolve was really brute force and slow,
this is a better solution, see problem page for explanation
"""

from math import floor, sqrt

LIMIT = 10000
result = 0


def d(n):
    res = 0
    r = floor(sqrt(n))
    if r * r == n:
        res = r + 1
        r -= 1
    else:
        res = 1
    f, step = 0, 0
    if n % 2 == 1:
        f, step = 3, 2
    else:
        f, step = 2, 1
    while f <= r:
        if n % f == 0:
            res += f + (n // f)
        f += step
    return res

for test in range(2, LIMIT):
    b = d(test)
    if b > test:
        if d(b) == test:
            result += test + b

print(result)
