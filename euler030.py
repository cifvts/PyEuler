#!/usr/bin/python

power_sum = 0
# Upper limit is a 6 digits number
for i in range(2, (9 ** 5) * 6):
    # I'm loving Python sugar
    if sum(int(j) ** 5 for j in str(i)) == i:
        # If you want to see the numbers
        # print(i)
        power_sum += i

print(power_sum)
