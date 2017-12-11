import operator
from typing import List

import pytest

from day06_pt1 import count_cycles


@pytest.mark.parametrize("values, expected_index, expected_value", [
    ([0], 0, 0),
    ([0, 1], 1, 1),
    ([0, 1, 7], 2, 7),
    ([0, 2, 7, 0], 2, 7),
    ([0, 2, 7, 5, 7], 2, 7),
    ([0, 2, 7, 5, 8], 4, 8),
])
def test_index_of_max(values: List[int], expected_index: int, expected_value: int):
    assert (expected_index, expected_value) == max(enumerate(values), key=operator.itemgetter(1))


@pytest.mark.parametrize("values, expected_cycles", [
    ([0, 2, 7, 0], 5),
    ([0, 5, 10, 0, 11, 14, 13, 4, 11, 8, 8, 7, 1, 4, 12, 11], 7864),
    ([1], 1),
    ([0], 1),
    ([0, 0, 0], 1),
])
def test_count_cycles(values: List[int], expected_cycles: int):
    assert expected_cycles == count_cycles(values)