import pytest

from day01 import sum_captcha


@pytest.mark.parametrize("captcha, solution", [
    ('1122', 3),
    ('1111', 4),
    ('1234', 0),
    ('91212129', 9),
])
def test_sum_captcha_with_step_1(captcha: str, solution: int):
    assert sum_captcha(captcha, step_size=1) == solution


@pytest.mark.parametrize("captcha, solution", [
    ('1212', 6),
    ('1221', 0),
    ('123425', 4),
    ('123123', 12),
    ('12131415', 4),
])
def test_sum_captcha_with_step_half_of_number_of_digits(captcha: str, solution: int):
    assert sum_captcha(captcha, step_size=len(captcha) // 2) == solution
