#!/usr/bin/env python3

def selection_sort(list):
    length = len(list)
    for i in range(length):
        min = i
        for j in range(i + 1, length):
            if list[j] < list[min]:
                min = j
        if min != i:
            list[i], list[min] = list[min], list[i]
    return list

list = [2, 4, 5, 0, 1, 12, 232, -1, 3]

print(selection_sort(list))
