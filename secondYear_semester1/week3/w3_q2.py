#!/usr/bin/env python3

#Q2. Using recursion, write a script to reverse an integer. you cannot use strings

def rev(n, r=0):
	if n < 1:
		return r
	ones = n % 10
	left_overs = n // 10
	r = (r * 10) + ones
	return rev(left_overs, r)

n = int(input())

print(rev(n))
