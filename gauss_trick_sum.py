from typing import Sequence


def gauss_trick_sum(sequence: Sequence[int]) -> int:
    if sequence[0] != 1:
        raise ValueError('sequence must start at one.')
    last = sequence[-1]
    return int(last * (last + 1) / 2)
