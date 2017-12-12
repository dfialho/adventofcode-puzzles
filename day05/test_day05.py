from typing import List

import pytest

from day05 import count_steps


@pytest.mark.parametrize("offsets, expected_step_count", [
    ([0, 3, 0, 1, -3], 5),
    ([1, 3, 0, 1, -3], 4),
    ([], 0),
    ([1], 1),
    ([0], 2),
    ([-1], 1),
    ([1, 0], 3),
    ([1, -3], 2),
])
def test_count_steps_part1(offsets: List[int], expected_step_count: int):
    assert expected_step_count == count_steps(offsets, lambda offset: +1)


@pytest.mark.parametrize("offsets, expected_step_count", [
    ([0, 3, 0, 1, -3], 10),
    ([1, 3, 0, 1, -3], 9),
    ([], 0),
    ([1], 1),
    ([0], 2),
    ([-1], 1),
    ([1, 0], 3),
    ([3, 0, 1, 1, -4], 6),
])
def test_count_steps_part2(offsets: List[int], expected_step_count: int):
    assert expected_step_count == count_steps(offsets, lambda offset: -1 if offset >= 3 else +1)
