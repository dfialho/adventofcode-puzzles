import pytest

from day09 import Parser


@pytest.mark.parametrize("stream, expected_score, expected_garbage_count", [
    ("{}", 1, 0),
    ("{{{}}}", 6, 0),
    ("{{},{}}", 5, 0),
    ("{{{},{},{{}}}}", 16, 0),
    ("{<{},{},{{}}>}", 1, 10),
    ("{<a>,<a>,<a>,<a>}", 1, 4),
    ("{{<ab>},{<ab>},{<ab>},{<ab>}}", 9, 8),
    ("{{<!!>},{<!!>},{<!!>},{<!!>}}", 9, 0),
    ("{{<a!>},{<a!>},{<a!>},{<ab>}}", 3, 17),
    ("{<>}", 1, 0),
    ("{<random characters>}", 1, 17),
    ("{<<<<>}", 1, 3),
    ("{<{!>}>}", 1, 2),
    ("{<!!>}", 1, 0),
    ("{<!!!>>}", 1, 0),
    ("{<{o\"i!a,<{i<a>}", 1, 10),
])
def test_parser(stream: str, expected_score: int, expected_garbage_count: int):
    assert (expected_score, expected_garbage_count) == Parser().parse(iter(stream))
