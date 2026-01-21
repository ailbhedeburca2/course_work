#!/usr/bin/env python3

from multiprocessing import *

def sayHi(n):
	print("Hi", n, "from process", current_process().pid)

def name():
	n = input("Enter your name: ")
	return n

def proc_num():
	procs = int(input("How many process would you like to run? "))
	return procs

def procEx():
	print("Hi from process", current_process().pid, "(main process)")
	n = name()
	p = proc_num()

	for i in range(p):
		proc = Process(target=sayHi, args=(n,))
		proc.start()
		#(Process(target=sayHi, args=(n))).start()
procEx()
