#!/usr/bin/env python3

#Q1. Write a function q1_sum() that takes a list as input
#and returns the sum of all even elements.

lists = [[1,0,2], [5,5,7], [9,4,3]]

def q1_sum(lists):

  total = 0

  for l in lists:
    for n in l:
      if n % 2 == 0:
        total += n

  return total

def main():

  answer = q1_sum(lists)
  print(answer)

if __name__ == '__main__':
  main()
