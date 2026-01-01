#!/usr/bin/env python3

#Q6. Write a function filter_star() to take the following dictionary
# and an integer as input. The function should return a new
# dictionary of items which match the specified star rating.
# Return No result found! if no match is found.


def filter_star(dic, int):

  new_dic = {}

  for x in dic:
    if len(dic[x]) == int:
      new_dic[x] = dic[x]
  if new_dic:
    return new_dic
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
