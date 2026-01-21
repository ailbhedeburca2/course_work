#!/usr/bin/env python3

from multiprocessing import *
import time

def greet(q):
	for i in range(5):
		print("(child process) Waiting for name to be sent ...")
		name = q.get()
		print("My name is", name, "I am number", i, "in the queue")

def sendName():
	q = Queue()

	names = ['Ailbhe', 'Tom', 'Jim', 'Ava', 'Cat']

	p1 = Process(target=greet, args=(q,))
	p1.start()

	for i in range(len(names)):
		time.sleep(3)
		print("(parent process) Okay, I'll send the name")
		q.put(names[i])

sendName()
