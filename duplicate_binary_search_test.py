from duplicate_binary_search import has_duplicates_using_binary_search


def test_has_duplicates_using_binary_search():
    assert has_duplicates_using_binary_search([1, 2, 3, 3, 4])
    assert not has_duplicates_using_binary_search([1, 2, 3, 4, 5])
