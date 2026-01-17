#!/usr/bin/env python3

import random

n = 10

list = [random.randint(-50, 50) for _ in range(10)]
largest = list[0]

i = 1
while i < n:
	if list[i] > largest:
		largest = list[i]
	i += 1

print(largest)
