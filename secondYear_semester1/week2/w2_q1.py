#!/usr/bin/env python3

#Q1. Create a class called Horse that takes their world ranking and
# current value in Euro as input. Attributes of the Horse class
# should not be accessed directly, only through instance methods.

#Create 100 horses and store them in a data structure of your choice.

#A horse's value in Euro is calculated based on their rank:.

#The horse with rank 100 is worth €1000
#The horse with rank 99 the same as horse 100 + 10%. For example,
# the horse with rank 99 will be worth: €1100

#The horse with rank 1 the same as horse 2 + 10%
#Create a menu for the user to allow them to enter the rank a horse
# a number of times. Each time the user enters a rank, the program
# should print out the rank and value of the horse using with
# suitable message. The message should be implemented in an instance
# method of the horse class called: display().

#If the user enters -1 it should display the rank and value of each horse in rank order from 1 to 100.

#If the rank of a horse is not found, print: "A horse with rank x was not found!"

class Horse(object):

	def __init__(self):
		self.__horses = {}

	def make_ranking(self):
		value = 1000
		for i in range(100, 0, -1):
			self.__horses[i] = value
			total = value * 0.1
			value += total
		return self.__horses

	def display(self, rank):
		table = self.make_ranking()
		if rank in table.keys():
			return f'Rank: {rank}, Value: {table[rank]:.2f}'
		return f'A horse with rank {rank} was not found'

	def get_table(self):
		table = self.make_ranking()
		for i in range(1, 101):
			print(f'Rank: {i}, Value: {table[i]:.2f}')

def main():

	h = Horse()

	while True:
		rank = int(input())
		if rank == -1:
			h.get_table()
			break
		print(h.display(rank))

if __name__ == '__main__':
	main()
