#!/usr/bin/python

"""
For resolve this, we have to find the maximum
Full Reptend Prime int he given limit. To do that, we need
to check if the 10 is a primitive root of p.

See http://mathworld.wolfram.com/FullReptendPrime.html for details
"""

from sys import exit

for p in range(999, 7, -2):
    for k in range(1, p):
        if (10 ** k) % p == 1:
            if k != p - 1:
                break
            else:
                print(p)
                exit(0)
