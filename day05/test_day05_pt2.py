import pytest

from day05_pt2 import count_steps


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
def test_count_steps(offsets: list, expected_step_count: int):
    assert expected_step_count == count_steps(offsets)
