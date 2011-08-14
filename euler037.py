#!/usr/bin/python

from math import sqrt, ceil, log10, pow, floor


def isPrime(x):
    if(x == 0 or x == 1):
        return 0
    if(x == 2 or x == 3 or x == 5 or x == 7):
        return 1
    if(x % 2 == 0):
        return 0
    for i in range(3, ceil(sqrt(x) + 1), 2):
        if x % i == 0:
            return 0
    return 1

prime_n = 9
count = 0
prime_sum = 0

while(count < 11):
    prime_n += 2
    if(isPrime(prime_n)):
        right = prime_n
        right = right // 10
        while(isPrime(right)):
            right = right // 10
        if(right):
            continue
        left = prime_n
        left = left % (pow(10, floor(log10(left))))
        while(isPrime(int(left))):
            left = left % (pow(10, floor(log10(left))))
        if(left):
            continue
        prime_sum += prime_n
        count += 1
print(prime_sum)
