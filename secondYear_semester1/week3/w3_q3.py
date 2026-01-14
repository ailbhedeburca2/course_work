#!/usr/bin/env python3

#Q3. Similar to Q2, write a script to reverse a string using recursion.

def rev(s):
	if not s:
		return s
	return s[-1] + rev(s[:-1])

s = input()

print(rev(s))
