#!/usr/bin/env python3

from multiprocessing import *
import time

def addTwoNums(q, a, b):
	time.sleep(3)
	q.put(a+b)

def twoNums():

	a = int(input("Input first number: "))
	b = int(input("Input second number: "))

	q = Queue()

	p1 = Process(target=addTwoNums, args=(q, a, b,))
	p1.start()

	print("Waiting for answer...")
	print(q.get())

twoNums()
