#!/usr/bin/python

from fractions import gcd

num = 1
den = 1

for c in range(1, 10):
    for b in range(1, c):
        for a in range(1, b):
            x = a * 10 + c
            y = c * 10 + b
            if (a / b) == (x / y):
                num *= a
                den *= b

print(den // gcd(den, num))
