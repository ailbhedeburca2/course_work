#!/usr/bin/env python3

import random

n = 10

list = [random.randint(-50, 50) for _ in range(10)]
smallest = list[0]

i = 1
while i < n:
	if list[i] < smallest:
		smallest = list[i]
	i += 1

print(smallest)
