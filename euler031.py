#!/usr/bin/python

LIMIT = 200
coins = [1, 2, 5, 10, 20, 50, 100, 200]


def rec_count(total, step):
    if total == LIMIT:
        return 1
    if total > LIMIT:
        return 0
    c = 0
    for x in coins:
        if x < step:
            continue
        c += rec_count(total + x, x)
    return c

count = 0
for x in coins:
    count += rec_count(x, x)
print(count)
