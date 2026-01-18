#!/usr/bin/env python3

import sys

s = sys.stdin.read().strip().split()

for x in s:
	new_str = ''
	new_str = x[0].upper() + x[1:-1] + x[-1].upper()
	print(new_str)
