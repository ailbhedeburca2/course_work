#!/usr/bin/env python3

n = int(input())

prev = 0
curr = 1

i = 0
while i < n:
	if prev < n:
		print(prev)
		p = curr
		curr = prev + curr
		prev = p
	i += 1
