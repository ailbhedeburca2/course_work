#!/usr/bin/env python3

def insertion_sort(list):
    length = len(list)
    for i in range(1, length):
        vals_to_sort = list[i]

        while i > 0 and vals_to_sort < list[i-1]:
            list[i-1], list[i] = list[i], list[i-1]
            i -= 1
    return list

list = [2, 4, 5, 0, 1, 12, 232, -1, 3]

print(insertion_sort(list))
