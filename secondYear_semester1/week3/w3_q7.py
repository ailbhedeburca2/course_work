#!/usr/bin/env python3

#Q7. Write a function that returns the length of a string. Make your function recursive.

def str_len(s, count=0):
    if not s:
        return count
    count += 1
    return str_len(s[:-1], count)

s = input()

print(str_len(s))
