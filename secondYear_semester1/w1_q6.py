#!/usr/bin/env python3

def filter_star(dic, int):

  for x in dic:
    if len(dic[x]) == int:
      return x
  return 'No result found!'

def main():

  dic = {
  'Luxury Chocolates': '*****',
  'Tasty Chocolates': '****',
  'Big Chocolates': '*****',
  'Generic Chocolates': '***'
  }

  int = 4

  answer = filter_star(dic, int)
  print(answer)

if __name__ == '__main__':
  main()
