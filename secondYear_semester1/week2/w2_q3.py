#!/usr/bin/env python3

#Q3. Write a Python function that takes a list of strings, and returns a new list
# where each string has been reversed and converted to uppercase.

def rev_upper(list):
	for i in range(len(list)):
		list[i] = list[i][::-1].upper()

	return list

def main():

	list = ['ailbhe', 'dog', 'cat', 'love']

	print(rev_upper(list))

if __name__ == '__main__':
	main()
