import pytest

from part2 import is_passphrase_valid


@pytest.mark.parametrize("passphrase, is_valid", [
    ("abcde fghij", True),
    ("abcde xyz ecdab", False),
    ("a ab abc abd abf abj", True),
    ("iiii oiii ooii oooi oooo", True),
    ("oiii ioii iioi iiio", False),
])
def test_moves(passphrase: str, is_valid: bool):
    assert is_valid == is_passphrase_valid(passphrase)
