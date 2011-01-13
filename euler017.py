#!/usr/bin/python

values = {}
values[1] = "one"
values[2] = "two"
values[3] = "three"
values[4] = "four"
values[5] = "five"
values[6] = "six"
values[7] = "seven"
values[8] = "eight"
values[9] = "nine"
values[10] = "ten"
values[11] = "eleven"
values[12] = "twelve"
values[13] = "thirteen"
values[14] = "fourteen"
values[15] = "fifteen"
values[16] = "sixteen"
values[17] = "seventeen"
values[18] = "eighteen"
values[19] = "nineteen"
values[20] = "twenty"
values[30] = "thirty"
values[40] = "forty"
values[50] = "fifty"
values[60] = "sixty"
values[70] = "seventy"
values[80] = "eighty"
values[90] = "ninety"

count = 0
for i in range(1, 1000 + 1):
    tmp = i
    if tmp // 1000:
        count += len(values[tmp // 1000]) + 8
        break
    if tmp // 100:
        count += len(values[tmp // 100]) + 10
        tmp %= 100
    if not tmp:
        count -= 3
    elif tmp in values:
        count += len(values[tmp])
    else:
        count += len(values[(tmp // 10) * 10])
        tmp %= 10
        count += len(values[tmp])

print(count)
