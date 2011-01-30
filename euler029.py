#!/usr/bin/python

power_list = set()

for a in range(2, 101):
    for b in range(2, 101):
        power_list.add(a ** b)

print(len(power_list))
