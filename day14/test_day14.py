import pytest

from day14 import build_grid, count_used


@pytest.mark.parametrize("key_str, expected_count", [
    ("flqrgnkx", 8108)
])
def test_count_used(key_str: str, expected_count: int):
    assert expected_count == count_used(build_grid(key_str))
