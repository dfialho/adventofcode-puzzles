import pytest

from sum_captcha_part1 import sum_captcha


@pytest.mark.parametrize("captcha, solution", [
    ('1122', 3),
    ('1111', 4),
    ('1234', 0),
    ('91212129', 9),
])
def test_sum_captcha(captcha: str, solution: int):
    assert sum_captcha(captcha) == solution
