from typing import List


def bubble_sort(unordered_iterable: List) -> List:
    iterable_length = len(unordered_iterable)
    result = unordered_iterable[:]
    while True:
        moved = 0
        for x in range(iterable_length - 1):
            l, r = result[x], result[x + 1]
            if l > r:
                result[x] = r
                result[x + 1] = l
                moved += 1
        if not moved:
            return result
