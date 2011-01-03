#!/usr/bin/python

TARGET = 600851475143

dividend = TARGET
factor = 3

while dividend > 1:
    while dividend % factor == 0:
        dividend //= factor
    factor += 2

print (factor - 2)
