#!/usr/bin/env python3

day = int(input())

if not 0 < day < 5 and not day < 7:
	print('Invalid input\nMust be between 0 and 6')
elif 0 < day < 5:
	print('weekday')
else:
	print('weekend')
