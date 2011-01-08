#!/usr/bin/python

"""
First attempt to resolve this, with a brute force algorithm,
it may not find the answer
"""

from math import sqrt

TARGET = 1000
LIMIT = int(sqrt(TARGET))
a, b, c = 0, 0, 0
m = 1
while(a + b + c != TARGET and m < LIMIT):
    m += 1
    a, b, c = 0, 0, 0
    n = 1
    while(a + b + c < TARGET and n < m):
        # This generate almost all the primitive Pythagorean triplets
        # if we're lucky the one we search for is primitive
        a = (m * m) - (n * n)
        b = 2 * m * n
        c = (m * m) + (n * n)
        n += 1

if a + b + c == TARGET:
    print(a * b * c)
else:
    print("Answer not found")
