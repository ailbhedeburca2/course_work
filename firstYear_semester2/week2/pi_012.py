#!/usr/bin/env python3

import sys
import math

n = sys.stdin.readline().strip()
n = int(n)

while n:
	print(f'{math.pi:.{n}f}')
	n = sys.stdin.readline().strip()

