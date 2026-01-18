#!/usr/bin/env python3

import sys

s = sys.stdin.readline().strip()

while s:
	if not len(s) <= 2:
		print(s[1:-1])
	s = sys.stdin.readline().strip()
