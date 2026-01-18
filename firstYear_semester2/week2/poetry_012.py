#!/usr/bin/env python3

import sys

poem = sys.stdin.read().strip().split('\n')

max_len = max(len(lines) for lines in poem)

for lines in poem:
	print(f'{lines:^{max_len}}')
