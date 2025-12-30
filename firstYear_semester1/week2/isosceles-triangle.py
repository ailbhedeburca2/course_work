#!/usr/bin/env python3

a = int(input())
b = int(input())
c = int(input())

# a = b, c
# a = c, b
# b = c, a

if a == b and a != c:
	print("True")
elif a == c and a != b:
	print("True")
elif b == c and b != a:
	print("True")
else:
	print("False")
