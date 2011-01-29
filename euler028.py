#!/usr/bin/python

count = 1
target = 3
step = 2
LIMIT = 1001

while step < LIMIT:
    for i in range(4):
        count += target
        target += step
    target += 2
    step += 2

print(count)
