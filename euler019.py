#!/usr/bin/python

months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
total = 0
sundays_count = 0

for year in range(1901, 2001):
    for m in range(len(months)):
        # 1 Jan 1900 was a Monday, 1 Jan 1901 was a Tuesday
        # so if Tuesday % 7 == 0 then Sunday % 7 == 5
        if total % 7 == 5:
            sundays_count += 1
        if (m == 1) and (year % 4 == 0):
            total += 1
        total += months[m]

print(sundays_count)
