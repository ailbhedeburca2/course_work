#!/usr/bin/env python3

#Q1. Write a function sum_q1() that takes an integer n as input and returns the sum of 0...n using recursion.

def sum(n):
	if n < 1:
		return n
	return n + sum(n - 1)

n = int(input())

print(sum(n))

