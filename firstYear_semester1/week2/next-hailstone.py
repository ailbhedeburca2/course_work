#!/usr/bin/env python3

#Write a python script named next-hailstone.py which outputs just
# the term following n in the Hailstone sequence.


n = int(input())

if n % 2 == 0:
	print(n//2)
else:
	print((n * 3) + 1)
