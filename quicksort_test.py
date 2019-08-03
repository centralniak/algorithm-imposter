from quicksort import quicksort


def test_quicksort():
    assert quicksort([5, 4, 3, 1, 2]) == [1, 2, 3, 4, 5]
    assert quicksort([3, 3, 2]) == [2, 3, 3]
