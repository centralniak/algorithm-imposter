from bubble_sort import bubble_sort


def test_bubble_sort_already_ordered():
    assert bubble_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]


def test_bubble_sort_needs_reordering():
    assert bubble_sort([5, 3, 2, 1, 4]) == [1, 2, 3, 4, 5]


def test_bubble_sort_has_duplicates():
    assert bubble_sort([1, 4, 4, 3, 5, 2]) == [1, 2, 3, 4, 4, 5]
