#!/usr/bin/python

from math import sqrt, ceil

palindrome = 999999
count = 0
f1 = 0
f2 = 0

while not (f1 * f2 == palindrome):
    f1 = 0
    f2 = 0
    radix = sqrt (palindrome)
    i = ceil (radix)
    exit
    while (i < 1000) and (not f1):
        if palindrome % i == 0:
            f1 = i
        i += 1

    if f1:
        i = ceil (radix)
        while (i > 99) and (not f2):
            if palindrome % i == 0:
                f2 = i
            i -= 1

    # ++ and -- don't exist in python
    count += 1
    if not (f1 * f2 == palindrome):
        if count % 100 == 0:
            palindrome -= 100001
            palindrome +=  90090
            palindrome +=   9900
        elif count % 10 == 0:
            palindrome -=  10010
            palindrome +=   9900
        else:
            palindrome -=   1100

print (f1, " * ", f2, " = ", palindrome)
