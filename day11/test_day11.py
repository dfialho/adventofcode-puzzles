from typing import List

import pytest

from day11 import Position, child_position


@pytest.mark.parametrize("child_steps, expected_position", [
    (['ne', 'ne', 'ne'], Position(0, 3, -3)),
    (['ne', 'ne', 'sw', 'sw'], Position(0, 0, 0)),
    (['ne', 'ne', 's', 's'], Position(2, 0, -2)),
    (['se', 'sw', 'se', 'sw', 'sw'], Position(2, -3, 1)),
])
def test_child_position(child_steps: List[str], expected_position: Position):
    assert expected_position == child_position(child_steps)


@pytest.mark.parametrize("position, expected_distance", [
    (Position(0, 3, -3), 3),
    (Position(0, 0, 0), 0),
    (Position(2, 0, -2), 2),
    (Position(2, -3, 1), 3),
    (Position(-2, -2, 4), 4),
])
def test_distance(position: Position, expected_distance: int):
    assert expected_distance == position.distance
