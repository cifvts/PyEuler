#!/usr/bin/python

from math import floor, sqrt

LIMIT = 28134


def isAbundant(n):
    max_t = floor(sqrt(n)) + 1
    sum_d = 1
    if n % 2 == 0:
        st, step = 2, 1
    else:
        st, step = 3, 2
    for i in range(st, max_t, step):
        if n % i == 0:
            sum_d += i + n // i
        if i == n / i:
            sum_d -= i
    return sum_d > n

""" Main """
abd_l = [0] * LIMIT
for i in range(12, LIMIT):
    if isAbundant(i):
        abd_l[i] = 1

sum_abd = 0
for i in range(1, LIMIT):
    abd = 0
    for j in range(12, (i // 2) + 1):
        if abd_l[j] and abd_l[i - j]:
            abd = 1
            break
    if not abd:
        sum_abd += i

print(sum_abd)
