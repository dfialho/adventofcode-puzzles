import pytest

from sum_captcha_part2 import sum_captcha


@pytest.mark.parametrize("captcha, solution", [
    ('1212', 6),
    ('1221', 0),
    ('123425', 4),
    ('123123', 12),
    ('12131415', 4),
])
def test_sum_captcha(captcha: str, solution: int):
    assert sum_captcha(captcha) == solution
