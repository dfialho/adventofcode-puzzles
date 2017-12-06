from typing import List

import pytest

from day06_pt1 import max_and_index, count_cycles


@pytest.mark.parametrize("values, expected_index, expected_value", [
    ([0], 0, 0),
    ([0, 1], 1, 1),
    ([0, 1, 7], 2, 7),
    ([0, 2, 7, 0], 2, 7),
    ([0, 2, 7, 5, 7], 2, 7),
    ([0, 2, 7, 5, 8], 4, 8),
])
def test_index_of_max(values: List[int], expected_index: int, expected_value: int):
    assert (expected_index, expected_value) == max_and_index(values)


@pytest.mark.parametrize("values, expected_cycles", [
    ([0, 2, 7, 0], 5),
])
def test_count_cycles(values: List[int], expected_cycles: int):
    assert expected_cycles == count_cycles(values)
