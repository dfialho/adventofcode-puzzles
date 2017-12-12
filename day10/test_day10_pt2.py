from typing import List

import pytest

from day10_pt2 import reverse, slide, knot_hash, hex_str, xor


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


@pytest.mark.parametrize("values, expected_result", [
    ([65, 27, 9, 1, 4, 3, 40, 50, 91, 7, 6, 0, 2, 5, 68, 22], 64),
])
def test_xor(values: List[int], expected_result: int):
    assert expected_result == xor(values)


@pytest.mark.parametrize("value, expected_str", [
    (4, "04"),
    (10, "0a"),
    (16, "10"),
])
def test_hex_str(value: int, expected_str: str):
    assert expected_str == hex_str(value)


@pytest.mark.parametrize("input_str, expected_hash_str", [
    ("", "a2582a3a0e66e6e86e3812dcb672a272"),
    ("AoC 2017", "33efeb34ea91902bb2f59c9920caa6cd"),
    ("1,2,3", "3efbe78a8d82f29979031a4aa0b16a9d"),
    ("1,2,4", "63960835bcdc130f0b66d7ff4f6a5a8e"),
])
def test_knot_hash(input_str: str, expected_hash_str: str):
    assert expected_hash_str == knot_hash(input_str)
