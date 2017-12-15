import pytest

from day14 import build_grid, count_used, count_groups


@pytest.mark.parametrize("key_str, expected_count", [
    ("flqrgnkx", 8108)
])
def test_count_used(key_str: str, expected_count: int):
    assert expected_count == count_used(build_grid(key_str))


@pytest.mark.parametrize("key_str, expected_count", [
    ("flqrgnkx", 1242)
])
def test_count_regions(key_str: str, expected_count: int):
    assert expected_count == count_groups(key_str)
