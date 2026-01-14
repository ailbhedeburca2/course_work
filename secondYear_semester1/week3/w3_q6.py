#!/usr/bin/env python3

#Q6. A pronic number (or otherwise called as heteromecic) is a number which is a product of two consecutive integers, that is, a number of
# the form n(n + 1). Create a function that determines whether a number is pronic or not.

def pronic(targ, n=0):
    if n * (n + 1) == targ or n * (n + 1) > targ:
        return n * (n + 1) == targ
    return pronic(targ, n + 1)

targ = int(input())

print(pronic(targ))


