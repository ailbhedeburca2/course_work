#!/usr/bin/env python3

import sys

s = sys.stdin.readline().strip()

while s:
	tokens = s.split()
	w1 = tokens[0].lower()
	w2 = tokens[1].lower()
	if w1 in w2:
		print('True')
	else:
		print('False')
	s = sys.stdin.readline().strip()
