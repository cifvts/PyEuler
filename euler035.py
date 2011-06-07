#!/usr/bin/python

from math import sqrt, ceil, floor, log10, pow

LIMIT = 1000000

def decimalShift(x):
    dec = x % 10;
    power = floor(log10(x))
    x //= 10;
    x += dec * int(pow(10, power))
    return x

sievebound = (LIMIT - 1) // 2
sieve = [0] * (sievebound)
crosslimit = (floor(sqrt(LIMIT)) - 1) // 2
for i in range(1, crosslimit):
    if not sieve[i]:
        for j in range(2 * i * (i + 1), sievebound, 2 * i + 1):
            sieve[j] = 1

count = 0
for i in range(sievebound):
    if not sieve[i]:
        prime = i * 2 + 1
        test = prime
        for j in range(ceil(log10(prime))):
            test = decimalShift(test)
            if test % 2 == 0 or sieve[(test - 1) // 2]:
                break
        if prime == test:
            count += 1

print(count)
