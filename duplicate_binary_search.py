from typing import Any, List

from binary_search import binary_search


def has_duplicates_using_binary_search(sorted_iterable: List[Any]) -> bool:
    for index, value in enumerate(sorted_iterable):
        if binary_search(sorted_iterable[index + 1:], value):
            return True
    return False
