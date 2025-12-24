#!/usr/bin/env python3

month = int(input())
day = int(input())

total = 0

i = 1
while i < month:
	total += 30
	i += 1

print(total + day)
