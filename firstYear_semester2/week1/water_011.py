#!/usr/bin/env python3

import sys

n = sys.stdin.readline().strip()
capacity = sys.stdin.readline().strip().split()

n = int(n)

count = 0
for num in capacity:
	n -= int(num)
	if n > -1:
		count += 1

print(count)
