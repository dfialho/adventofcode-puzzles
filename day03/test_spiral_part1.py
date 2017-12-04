import pytest

from spiral import moves, moves2

cases = [
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
]


@pytest.mark.parametrize("n, solution", cases)
def test_moves(n: int, solution: int):
    assert solution == moves(n)


@pytest.mark.parametrize("n, solution", cases)
def test_moves2(n: int, solution: int):
    assert solution == moves2(n)

