#!/usr/bin/env python3

n = input()

len = len(n)

if n[len - 1] == '1' and n != '11':
	print('st')
elif n[len - 1] == '2' and n != '12':
	print('nd')
elif n[len - 1] == '3' and n != '13':
	print('rd')
else:
	print('th')
