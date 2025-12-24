#!/usr/bin/env python3

n = int(input())

ones = n % 10
hundereds = n // 100

tens = (n - (100 * hundereds) - ones) // 10

print(hundereds)
print(tens)
print(ones)
