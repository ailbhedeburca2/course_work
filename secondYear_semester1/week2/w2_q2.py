#!/usr/bin/env python3

#Q2. Write a Python function that takes a list of numbers and returns a new list with each number squared.

def squared(list):
	for i in range(len(list)):
		list[i] = list[i] ** 2

	return list

def main():

	list = [1, 2, 3, 4, 5]

	print(squared(list))

if __name__ == '__main__':
	main()
