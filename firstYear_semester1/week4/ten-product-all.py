#!/usr/bin/env python3

n = 10

total = 1
list = [-1, 4, 8, 2, 1, -9, 5, 6, 9, 1]

i = 0
while i < n:
	total *= list[i]
	i += 1

print(total)
