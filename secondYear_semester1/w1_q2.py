#!/usr/bin/env python3

s = 'This is DCU!'

def move_vow(s):

  vowels = 'aeiouAEIOU'
  v = ''
  c = ''

  for letters in s:
    if letters in vowels:
      v += letters
    else:
      c += letters

  new_s = v + c
  return new_s

def main():

  answer = move_vow(s)
  print(answer)

if __name__ == '__main__':
  main()
