from typing import List

import pytest

from day06 import count_cycles


@pytest.mark.parametrize("values, expected_cycles", [
    ([0, 2, 7, 0], 5),
    ([0, 5, 10, 0, 11, 14, 13, 4, 11, 8, 8, 7, 1, 4, 12, 11], 7864),
    ([1], 1),
    ([0], 1),
    ([0, 0, 0], 1),
])
def test_count_cycles(values: List[int], expected_cycles: int):
    assert expected_cycles == count_cycles(values)[0]


@pytest.mark.parametrize("values, expected_cycles", [
    ([0, 2, 7, 0], 4),
    ([1], 1),
    ([0], 1),
    ([0, 0, 0], 1),
])
def test_loop_size(values: List[int], expected_cycles: int):
    assert expected_cycles == count_cycles(values)[1]
