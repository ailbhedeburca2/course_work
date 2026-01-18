#!/usr/bin/env python3

import sys

strs = sys.stdin.read().strip().split('\n')
target = 'm'

for s in strs:
	output = ''
	i = 0
	while i < len(s) and s[i] != target:
		output += s[i]
		i += 1
	letter = s[i].upper()
	print(output + letter + s[i + 1:])
