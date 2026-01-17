#!/usr/bin/env python3

weight = int(input())
height = int(input())

bmi = weight / (height * height) * 10000

if bmi < 18.5:
	print('underweight')
elif 18.5 < bmi < 24.9:
	print('normal')
elif 25 < bmi < 29.9:
	print('overweight')
elif bmi >= 30:
	print('obese')
