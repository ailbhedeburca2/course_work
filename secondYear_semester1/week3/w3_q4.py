#!/usr/bin/env python3

#Q4. Write a script to inverse a list of numbers using recursion.

def rev(l):
	if not l:
		return l
	return [l[-1]] + rev(l[:-1])

l = list(input())

print(rev(l))
