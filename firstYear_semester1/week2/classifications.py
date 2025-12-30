#!/usr/bin/env python3

def first(mark):
	return mark >= 70

def second(mark):
	return 50 <= mark <= 69

def third(mark):
	return 40 <= mark <= 49

def fail(mark):
	return mark < 40

mark = int(input())

print(f"first: {first(mark)}")
print(f"second: {second(mark)}")
print(f"third: {third(mark)}")
print(f"fail: {fail(mark)}")
