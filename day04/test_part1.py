import pytest

from part1 import is_passphrase_valid


@pytest.mark.parametrize("passphrase, is_valid", [
    ("aa bb cc dd ee", True),
    ("aa bb cc dd ee aa", False),
    ("aa bb cc dd ee aaa", True),
])
def test_moves(passphrase: str, is_valid: bool):
    assert is_valid == is_passphrase_valid(passphrase)
