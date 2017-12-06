from typing import List

import pytest

from day06_pt2 import loop_size


@pytest.mark.parametrize("values, expected_cycles", [
    ([0, 2, 7, 0], 4),
    ([1], 1),
    ([0], 1),
    ([0, 0, 0], 1),
])
def test_loop_size(values: List[int], expected_cycles: int):
    assert expected_cycles == loop_size(values)
