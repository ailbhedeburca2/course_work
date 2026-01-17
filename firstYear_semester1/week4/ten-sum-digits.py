#!/usr/bin/env python3

import random

n = 10

nums = [random.randint(-50, 50) for _ in range(10)]
total = 0
print(nums)

i = 0
while i < n:
	num = str(nums[i])
	l = len(num)
	digit = int(num[l - 1])
	total += digit
	i += 1

print(total)
