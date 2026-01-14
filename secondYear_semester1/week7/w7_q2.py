#!/usr/bin/env python3


def hash(str):
    length = len(str) - 1
    a = 27
    res = 0
    for l in str:
        res += a * (ord(l) ** length)
        length -= 1
    return res

def compress(code):
    return code % 11

def insert(str, bucket):
    s = hash(str)
    c = compress(s)
    for i in range(len(bucket)):
        if c == i:
            bucket[i].append(str)
    return bucket


code = hash('stop')
print(compress(code))
code = hash('pots')
print(compress(code))
code = hash('tops')
print(compress(code))
code = hash('spot')
print(compress(code))
bucket = [[] for _ in range(10)]
words = ['stop', 'pots', 'tops', 'spot']
for word in words:
    print(insert(word, bucket))
