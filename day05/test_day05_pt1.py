import pytest

from day05_pt1 import count_steps


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
def test_count_steps(offsets: list, expected_step_count: int):
    assert expected_step_count == count_steps(offsets)
