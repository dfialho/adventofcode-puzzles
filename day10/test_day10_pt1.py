from typing import List

import pytest

from day10_pt1 import reverse, slide


@pytest.mark.parametrize("elements, length, reversed_list", [
    ([0, 1, 2, 3, 4], 3, [2, 1, 0, 3, 4]),
    ([0, 1, 2, 3, 4], 5, [4, 3, 2, 1, 0]),
])
def test_reverse(elements: List[int], length: int, reversed_list: List[int]):
    assert reversed_list == reverse(elements, length)


@pytest.mark.parametrize("elements, offset, expected_result", [
    ([0, 1, 2, 3, 4], 0, [0, 1, 2, 3, 4]),
    ([0, 1, 2, 3, 4], 1, [1, 2, 3, 4, 0]),
    ([0, 1, 2, 3, 4], 2, [2, 3, 4, 0, 1]),
    ([0, 1, 2, 3, 4], 3, [3, 4, 0, 1, 2]),
    ([0, 1, 2, 3, 4], 4, [4, 0, 1, 2, 3]),
    ([0, 1, 2, 3, 4], 5, [0, 1, 2, 3, 4]),
    ([0, 1, 2, 3, 4], 6, [1, 2, 3, 4, 0]),
])
def test_slide(elements: List[int], offset: int, expected_result: List[int]):
    assert expected_result == slide(elements, offset)
