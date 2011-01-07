#!/usr/bin/python

limit = 100

sum_sq = ((limit + 1) * limit) / 2
sum_sq *= sum_sq
sq_sum = (limit * (limit + 1) * ((limit * 2) + 1)) / 6

print (int(sum_sq - sq_sum))
