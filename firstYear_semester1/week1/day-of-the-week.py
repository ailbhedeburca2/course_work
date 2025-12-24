#!/usr/bin/env python3

month = int(input())
day = int(input())

total = 0

i = 1
while i < month:
	total += 30
	i += 1

total += day
day_of_week = total % 7

if day_of_week == 0:
	print(7)
else:
	print(day_of_week)
