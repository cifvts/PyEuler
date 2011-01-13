#!/usr/bin/python

from math import pow

x = int(pow(2, 1000))

a = str(x)
res = 0
for i in range(len(a)):
    res += int(a[i])

print(res)
