#!/usr/bin/python

from math import pow

LIMIT = 1000000
palindrome_sum = 0

def is_palindrome(res):
	return res == res[::-1]

def binary(x):
	res = []
	while(x):
		res.insert(0, x % 2)
		x //= 2
	return res

for palindrome in range(1, LIMIT):
	if(is_palindrome(list(str(palindrome)))):
		binary_n = binary(palindrome)
		if(is_palindrome(binary_n)):
			palindrome_sum += palindrome 

print(palindrome_sum)
