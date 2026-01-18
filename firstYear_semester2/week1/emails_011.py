#!/usr/bin/env python3

import sys

emails = sys.stdin.read().strip().split()

for e in emails:
	last_name = ''
	names = e.split('@')
	tokens = names[0].split('.')
	first_name = tokens[0]
	last_names = tokens[1]
	i = 0
	while not last_names[i].isdigit():
		last_name += last_names[i]
		i += 1
	print(first_name[0].upper() + first_name[1:], last_name[0].upper() + last_name[1:])
