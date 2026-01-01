#!/usr/bin/env python3

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
