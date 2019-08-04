from typing import List


def selection_sort(unordered_iterable: List) -> List:
    iterable_len = len(unordered_iterable)
    result = unordered_iterable[:]
    for i in range(iterable_len):
        smallest_value = float('inf')
        smallest_index = None
        for j in range(i, iterable_len):
            if result[j] < smallest_value:
                smallest_value = result[j]
                smallest_index = j
        result.pop(smallest_index)
        result = result[:i] + [smallest_value] + result[i:]
    return result
