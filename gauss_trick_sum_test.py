from pytest import raises

from gauss_trick_sum import gauss_trick_sum


def test_starts_at_one():
    list_1_to_10 = list(range(1, 11))
    assert gauss_trick_sum(list_1_to_10) == sum(list_1_to_10)


def test_does_not_start_at_one():
    list_2_to_12 = list(range(2, 13))
    with raises(ValueError):
        gauss_trick_sum(list_2_to_12)
