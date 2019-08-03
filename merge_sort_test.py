from merge_sort import merge_sort


def test_merge_sort():
    # even element count
    assert merge_sort([5, 4, 2, 1]) == [1, 2, 4, 5]

    # uneven element count
    assert merge_sort([3, 4, 5, 1, 2, ]) == [1, 2, 3, 4, 5]
