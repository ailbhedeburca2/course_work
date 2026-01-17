#!/usr/bin/env python3

import random

n = 10

list = [random.randint(-50, 50) for _ in range(10)]

i = 0
while i < n:
	if list[i] > 0:
		smallest = list[i]
	i += 1

i = 0
while i < n:
	if list[i] > 0 and list[i] < smallest:
		smallest = list[i]
	i += 1

print(smallest)
