#!/usr/bin/env python3

import sys

s = sys.stdin.read().strip().split()

for x in s:
	if len(x) % 2 == 0:
		print('No middle character!')
	else:
		i = len(x) // 2
		print(x[i])
