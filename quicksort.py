from typing import List


def quicksort(unordered_iterable: List) -> List:
    # @TODO: use median as the pivot to speed things up
    pivot = unordered_iterable.pop()
    left, right = [], []
    for value in unordered_iterable:
        if value < pivot:
            left.append(value)
        else:
            right.append(value)
    if len(left) > 1:
        left = quicksort(left)
    if len(right) > 1:
        right = quicksort(right)
    return left + [pivot] + right
