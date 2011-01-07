#!/usr/bin/python

MAX = 4000000

result = 0
ancestor = 0
tmp = 0
current = 2

while current < MAX:
    tmp = current
    result += current
    current = (current * 4) + ancestor
    ancestor = tmp

print(result)
