#!/usr/bin/env python3

from math import sqrt

x1 = int(input())
y1 = int(input())
r1 = int(input())

x2 = int(input())
y2 = int(input())
r2 = int(input())

distance = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

if distance < r1 + r2:
	print('yes')
else:
	print('no')

