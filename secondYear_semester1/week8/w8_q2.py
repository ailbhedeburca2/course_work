#!/usr/bin/env python3

def quick_sort(list):
    length = len(list)
    if length <= 1:
        return list
    pivot = list.pop()
    left = []
    right = []
    for items in list:
        if items < pivot:
            left.append(items)
        else:
            right.append(items)
    return quick_sort(left) + [pivot] + quick_sort(right)

list = [2, 4, 5, 0, 1, 12, 232, -1, 3]

print(quick_sort(list))
