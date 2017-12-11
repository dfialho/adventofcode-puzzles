import pytest

from day09_pt2 import Parser


@pytest.mark.parametrize("stream, expected_garbage_count", [
    ("{}", 0),
    ("{{{}}}", 0),
    ("{{},{}}", 0),
    ("{{{},{},{{}}}}", 0),
    ("{<{},{},{{}}>}", 10),
    ("{<a>,<a>,<a>,<a>}", 4),
    ("{{<ab>},{<ab>},{<ab>},{<ab>}}", 8),
    ("{{<!!>},{<!!>},{<!!>},{<!!>}}", 0),
    ("{{<a!>},{<a!>},{<a!>},{<ab>}}", 17),
    ("{<>}", 0),
    ("{<random characters>}", 17),
    ("{<<<<>}", 3),
    ("{<{!>}>}", 2),
    ("{<!!>}", 0),
    ("{<!!!>>}", 0),
    ("{<{o\"i!a,<{i<a>}", 10),
])
def test_find_odd(stream: str, expected_garbage_count: int):
    assert expected_garbage_count == Parser().parse(iter(stream))
