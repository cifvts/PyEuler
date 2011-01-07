#!/usr/bin/python

from math import sqrt, ceil

def isPrime (x):
    for i in range (3, ceil (sqrt (x) + 1), 2):
        if x % i == 0:
            return 0
    return 1

# 2 already count
count = 1
# we start from 3
test = 3
while (count < 10001):
    if isPrime (test):
        count += 1
    test += 2

print (test - 2)
