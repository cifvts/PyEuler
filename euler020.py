#!/usr/bin/python

from math import factorial

fact = str(factorial(100))

result = 0
for i in range(len(fact)):
    result += int(fact[i])

print(result)
