#!/usr/bin/env python3

def bubble_sort(list):
    length = len(list)
    for i in range(length):
        for j in range(i + 1, length):
            if list[j] < list[i]:
                list[j], list[i] = list[i], list[j]
    return list

list = [2, 4, 5, 0, 1, 12, 232, -1, 3]

print(bubble_sort(list))
