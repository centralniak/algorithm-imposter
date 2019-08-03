from math import ceil
from typing import List, TypeVar

T = TypeVar('T')


def binary_search(sorted_iterable: List[T], value: T) -> bool:
    if not sorted_iterable:
        return False

    while sorted_iterable:
        iterable_len = len(sorted_iterable)
        if iterable_len == 1:
            return sorted_iterable[0] == value

        split_at = ceil(iterable_len / 2)
        l, r = sorted_iterable[0:split_at], sorted_iterable[split_at:]
        l_max = l[-1]

        if l_max >= value:
            sorted_iterable = l
        else:
            sorted_iterable = r

    return False
