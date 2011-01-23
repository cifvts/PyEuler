#!/usr/bin/python

name_file = open('./names.txt', 'r')

line = name_file.readline()
name_file.close()
# Split, sort name and join
names = line.split(',')
names.sort()
line = ','.join(names)

total = 0
n_name = 1
word = 0
for i in range(len(line)):
    if line[i] == ',' or i == len(line) - 1:
        total += word * n_name
        n_name += 1
        word = 0
    elif line[i] != '"':
        word += ord(line[i]) - 64

print(total)
