#!/usr/bin/env python3


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
