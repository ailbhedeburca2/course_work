#!/usr/bin/env python3

import sys

#digits
#lowercase
#uppercase
#special characters

def digit(p):
	for x in p:
		if x.isdigit():
			return x.isdigit()
	return False

def lower(p):
	for x in p:
		if 'a' <= x <= 'z':
			return 'a' <= x <= 'z'
	return False

def upper(p):
	for x in p:
		if 'A' <= x <= 'Z':
			return 'A' <= x <= 'Z'
	return False

def sc(p):
	chars = '!"£$%^&*()_-+=[]{}~#@\'\\:;?/>.<,|'
	for x in p:
		if x in chars:
			return x in chars
	return False

passwords = sys.stdin.read().strip().split('\n')

for p in passwords:
	count = 0
	if digit(p):
		count += 1
	if lower(p):
		count += 1
	if upper(p):
		count += 1
	if sc(p):
		count += 1
	print(count)
