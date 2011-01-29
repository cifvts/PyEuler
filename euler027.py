#!/usr/bin/python

"""
I don't have found a clever solution, this is a brute force analysis
"""

from math import sqrt, ceil

prime_list = [0] * 20000


def isPrime(x):
    if x < 0:
        return 0
    if x % 2 == 0:
        return 0
    if prime_list[x]:
        return 1
    for i in range(3, ceil(sqrt(x)), 2):
        if x % i == 0:
            return 0
    prime_list[x] = 1
    return 1

max_c, max_a, max_b = 0, 0, 0
for a in range(-999, 1000):
    for b in range(-999, 1000):
        c = 0
        test = c ** 2 + a * c + b
        while isPrime(test):
            c += 1
            test = c ** 2 + a * c + b
        if c - 1 > max_c:
            max_c, max_b, max_a = c - 1, b, a

print(max_a, max_b, max_c, max_a * max_b)
