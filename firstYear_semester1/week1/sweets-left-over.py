#!/usr/bin/env python3

num_sweets = int(input())

left_overs = num_sweets // 10

total = num_sweets - (10 * left_overs)

print(total)
