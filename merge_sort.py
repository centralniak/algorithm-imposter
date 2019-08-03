from math import ceil
from typing import List


def merge_sort(unordered_iterable: List) -> List:
    iterable_len = len(unordered_iterable)
    if iterable_len < 2:
        return unordered_iterable

    split_at = ceil(iterable_len / 2)
    l, r = unordered_iterable[0:split_at], unordered_iterable[split_at:]

    if len(l) > 1:
        l = merge_sort(l)
        r = merge_sort(r)

    sorted = []
    left_index, right_index = 0, 0
    left_len = len(l)
    right_len = len(r)
    while left_index < left_len and right_index < right_len:
        left_value = l[left_index]
        right_value = r[right_index]
        if left_value > right_value:
            right_index += 1
            sorted.append(right_value)
        else:
            left_index += 1
            sorted.append(left_value)
    sorted += l[left_index:] + r[right_index:]

    return sorted
