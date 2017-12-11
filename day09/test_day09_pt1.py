import pytest

from day09_pt1 import Parser


@pytest.mark.parametrize("stream, expected_group_count", [
    ("{}", 1),
    ("{{{}}}", 6),
    ("{{},{}}", 5),
    ("{{{},{},{{}}}}", 16),
    ("{<{},{},{{}}>}", 1),
    ("{<a>,<a>,<a>,<a>}", 1),
    ("{{<ab>},{<ab>},{<ab>},{<ab>}}", 9),
    ("{{<!!>},{<!!>},{<!!>},{<!!>}}", 9),
    ("{{<a!>},{<a!>},{<a!>},{<ab>}}", 3),
])
def test_find_odd(stream: str, expected_group_count: int):
    assert expected_group_count == Parser().parse(iter(stream))
