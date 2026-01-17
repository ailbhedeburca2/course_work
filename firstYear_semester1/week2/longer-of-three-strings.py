#!/usr/bin/env python3

s1 = input()
s2 = input()
s3 = input()

ls1 = len(s1)
ls2 = len(s2)
ls3 = len(s3)

if ls1 > ls2 and ls1 > ls3:
	print(s1)
elif ls2 > ls1 and ls2 > ls3:
	print(s2)
else:
	print(s3)
