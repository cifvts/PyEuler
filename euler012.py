#!/usr/bin/python

from math import sqrt

""" Our limit """
LIMIT = 500
""" We start from 6 """
test = 1 + 2 + 3
""" Next to add """
add = 4
div_count = 0
while div_count < LIMIT:
    div_count = 1
    test += add
    add += 1
    tmp = test
    for i in range(2, int(sqrt(test))):
        factor_count = 0
        while tmp % i == 0:
            tmp //= i
            factor_count += 1
        div_count *= (factor_count + 1)

print (test)
