#!/usr/bin/env python3

#Q5. Write a function histogram() that takes a list of numbers and
# a character as input.

#The function should print a new line per argument in list.
#The length of the lines corresponds to the numbers in the list
# passed as an argument.

def histogram(list, char):

  s = ''

  for x in list:
    s += ' ' + x * char

  return s[1:]

def main():

  list = [6,2,15,3,20,5]
  char = '='

  answer = histogram(list, char)
  print(answer)

if __name__ == '__main__':
  main()
