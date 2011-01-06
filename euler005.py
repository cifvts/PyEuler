#!/usr/bin/python

from math import pow, sqrt, log, floor
from functools import reduce

LIMIT = 21

"""
Python version of my old first attempt to solve this
"""
factors = [0] * LIMIT

for dividend in range (2, LIMIT):
    x = dividend
    for i in range (2,x):
        factor = 2
        while i > 1:
            count = 0
            while i % factor == 0:
                i //= factor
                count += 1
            if count > factors[factor]:
                factors[factor] = count
            factor += 1

result = 1
for j in range (2, LIMIT):
    result *= pow (j, factors[j])

print (int (result))

"""
Second version, using a better approch: in this case we calculate
the maximum factor exponents using log function
"""

def isPrime (x):
    if x % 2 == 0:
        return 0
    test = range (3, int(sqrt (x)) + 1, 2)
    for i in test:
        if x % i == 0:
            return 0
    return 1

result = 1
result *= pow ( 2, floor(log (LIMIT - 1) / log (2)))
for i in range (3, LIMIT, 2):
    if isPrime (i):
        result *= pow (i, floor (log (LIMIT - 1) / log (i)))

print (int (result))

"""
Beautiful solution from user EyeCon, found in projecteuler.net
problem 5 forum. This is really interesting and useful for understand
the possibilities of Python
"""
def gcd(a, b):
    while(b != 0):
        a, b = b, a%b
    return a
 
def lcm(a,b):
    return a * b / gcd(a, b)

print (int(reduce(lcm, range(2, 21))))
