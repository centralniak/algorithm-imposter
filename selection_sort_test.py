from selection_sort import selection_sort


def test_selection_sort():
    assert selection_sort([1, 2, 3]) == [1, 2, 3]
    assert selection_sort([3, 2, 1]) == [1, 2, 3]
    assert selection_sort([1, 5, 5, 4, 2]) == [1, 2, 4, 5, 5]
