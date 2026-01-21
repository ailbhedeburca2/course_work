#!/usr/bin/env python3

from multiprocessing import *

def sayHi(lock, name, hole):
	lock.acquire()
	print("Hi, I'm digger", name, "and I have to dig hole", hole)
	lock.release()

def assignDiggers():
	lock = Lock()

	seq = 'ABCDEFGHIJ'

	for i in range(len(seq)):
		Process(target=sayHi, args=(lock, seq[i], i)).start()

assignDiggers()
