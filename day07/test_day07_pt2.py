from typing import List

import pytest

from day07_pt2 import find_odd


@pytest.mark.parametrize("values, expected_odd, expected_normal", [
    ([2, 2, 2, 3], 3, 2),
    ([2, 2, 2, 1], 1, 2),
    ([2, 2, 1], 1, 2),
    ([1, 2, 1], 2, 1),
    ([1, 2, 2], 1, 2),
])
def test_find_odd(values: List[int], expected_odd: int, expected_normal: int):
    assert (expected_odd, expected_normal) == find_odd(values)

