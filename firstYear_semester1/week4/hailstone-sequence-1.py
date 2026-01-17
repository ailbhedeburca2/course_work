#!/usr/bin/env python3

n = int(input())
m = int(input())

print(m)

i = 0
while i < n - 1:
	if m % 2 == 0:
		print(m // 2)
		m = m // 2
	else:
		print((m * 3) + 1)
		m = (m * 3) + 1
	i += 1

