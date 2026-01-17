#!/usr/bin/env python3

import random

n = 10

list = [random.randint(1, 100) for _ in range(10)]

total = 0

i = 0
while i < n:
	total += list[i]
	i += 1

print(total)
