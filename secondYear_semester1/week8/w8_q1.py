#!/usr/bin/env python3

def merge_sort(list):
    length = len(list)
    if length <= 1:
        return list
    middle = length // 2
    left = merge_sort(list[:middle])
    right = merge_sort(list[middle:])
    return merge(left, right)

def merge(left, right):
    i = j = 0
    result = []
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

list = [2, 4, 5, 0, 1, 12, 232, -1, 3]

print(merge_sort(list))
