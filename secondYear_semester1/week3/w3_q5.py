#!/usr/bin/env python3

#Q5. Create a function that returns the product of two integers. This process of
#multiplication can be achieved via repetitive addition, thus, the process can be done recursively.

def mul(n, m):
    if m == 0:
        return 0
    if n < 0 and m < 0:
        return mul(-n, -m)
    elif m < 0:
        return mul(-n, -m)
    return n + mul(n, m - 1)

a = int(input())
b = int(input())

print(mul(a, b))
