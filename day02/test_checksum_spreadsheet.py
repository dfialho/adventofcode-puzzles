import pytest

from checksum_spreadsheet import difference, even_division


@pytest.mark.parametrize("row, expected_difference", [
    ([5, 1, 9, 5], 8),
    ([7, 5, 3], 4),
    ([2, 4, 6, 8], 6),
])
def test_difference(row: list, expected_difference: int):
    assert difference(row) == expected_difference


@pytest.mark.parametrize("row, expected_difference", [
    ([5, 9, 2, 8], 4),
    ([9, 4, 7, 3], 3),
    ([3, 8, 6, 5], 2),
    ([7, 8, 6, 5], 0),
    ([7, 8, 6, 3], 2),
    ([5, 8, 6, 5], 1),
])
def test_even_division(row: list, expected_difference: int):
    assert even_division(row) == expected_difference
