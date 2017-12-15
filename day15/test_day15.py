import pytest

from day15 import judge, generator


@pytest.mark.parametrize("seed_a, seed_b, match_count", [
    (65, 8921, 588)
])
def test_count_used(seed_a: int, seed_b: int, match_count: int):
    assert match_count == judge(
        generator(seed_a, factor=16807),
        generator(seed_b, factor=48271)
    )
