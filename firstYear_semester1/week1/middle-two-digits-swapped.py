#!/usr/bin/env python3

n = int(input())

new_n = n // 100
middle = new_n % 100

tens = middle % 10
ones = middle // 10

print((tens * 10) + ones)
