#!/usr/bin/python

from math import sqrt, ceil, floor

LIMIT = 2000000

"""
This is the first, brute force method, we search for primes,
and put them into an array, so we can use as test later.
This is not fast, and do millons mod test
"""


def isPrime(x):
    i = 0
    while primeList[i] <= sqrt(x):
        if x % primeList[i] == 0:
            return 0
        i += 1
    primeList.append(x)
    return 1

primeList = [2]
result = 2
prime = 3
while prime < LIMIT:
    if isPrime(prime):
        result += prime
    prime += 2

print (result)

"""
This method use an optimized Sieve of Eratosthenes algorithm,
it will search only for odd number. More explanation in
Project Euler site
"""

sievebound = (LIMIT - 1) // 2
sieve = [0] * (sievebound)
crosslimit = (floor(sqrt(LIMIT)) - 1) // 2
for i in range(1, crosslimit):
    if not sieve[i]:
        for j in range(2 * i * (i + 1), sievebound, 2 * i + 1):
            sieve[j] = 1
result = 2
for i in range(1, sievebound):
    if not sieve[i]:
        result += (2 * i + 1)
print(result)
