#!/usr/bin/env python3

home = int(input())
away = int(input())

if home == away:
	print('Draw')
elif home > away:
	print('Home win')
else:
	print('Away win')
