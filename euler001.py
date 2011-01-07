#!/usr/bin/python

LIMIT = 999


def sumDivisibleBy(step):
    p = LIMIT // step
    return step * (p * (p + 1)) // 2

print(sumDivisibleBy(3) + sumDivisibleBy(5) - sumDivisibleBy(15))
