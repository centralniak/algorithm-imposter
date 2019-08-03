from binary_search import binary_search


def test_binary_search_zero_elements():
    assert not binary_search([], 1)


def test_binary_search_one_element():
    assert binary_search([1], 1)
    assert not binary_search([2], 1)


def test_binary_search_many_elements():
    assert binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5)
    assert not binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 20)
