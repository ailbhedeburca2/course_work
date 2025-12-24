#!/usr/bin/env python3

meters = int(input())

left_overs = meters % 1000

if left_overs < 500:
	print(meters // 1000)
else:
	print((meters // 1000) + 1)
