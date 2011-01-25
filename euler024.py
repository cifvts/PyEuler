#!/usr/bin/python

"""
Solution based on Algorithm L by Donald Knuth,
see The Art of Computer Programming vol. 4
"""


def next(perm):
    tmp = list(perm)
    k = lastNotLast(tmp)
    if not k:
        return ''
    tmp = increase(k, tmp)
    tmp = first(k, tmp)
    return tmp


def lastNotLast(perm):
    l = len(perm) - 1
    while l and perm[l] < perm[l - 1]:
        l -= 1
    return l


def increase(k, perm):
    minmax = k
    tmp = list(perm)
    while minmax < len(perm) and tmp[minmax] > tmp[k - 1]:
        minmax += 1
    ch = tmp[k - 1]
    tmp[k - 1] = tmp[minmax - 1]
    tmp[minmax - 1] = ch
    return tmp


def first(k, perm):
    tmp = list(perm[:k])
    tmp1 = list(perm[k:])
    tmp1.reverse()
    tmp.extend(tmp1)
    return tmp


word = '0123456789'
for i in range(1, 1000000):
    word = next(word)

print(word)


"""
Really fast solution, we don't need to generate all the permutations
but we solve with a bit of analisys
"""
from math import factorial

word = '0123456789'
perm = []
limit = 1000000
fact = len(word) - 1
for i in range(fact, -1, -1):
    count = 0
    while limit > factorial(i):
        limit -= factorial(i)
        count += 1
    perm.append(word[count])
    word = word[:count] + word[count + 1:]

print(perm)
