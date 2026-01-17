#!/usr/bin/env python3

import random

n = 10

list = [random.randint(-50, 50) for _ in range(10)]
total = 0

i = 0
while i < n:
	if list[i] < 0:
		total += list[i] * -1
	else:
		total += list[i]
	i += 1

print(total)
