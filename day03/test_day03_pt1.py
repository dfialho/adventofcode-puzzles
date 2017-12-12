import pytest

from day03_pt1 import count_moves


@pytest.mark.parametrize("n, solution", [
    (1, 0),
    (2, 1),
    (3, 2),
    (4, 1),
    (7, 2),
    (8, 1),
    (9, 2),
    (10, 3),
    (13, 4),
    (15, 2),
    (24, 3),
    (25, 4),
    (26, 5),
    (27, 4),
    (30, 5),
    (31, 6),
    (45, 4),
    (47, 4),
    (43, 6),
])
def test_count_moves(n: int, solution: int):
    assert solution == count_moves(n)
