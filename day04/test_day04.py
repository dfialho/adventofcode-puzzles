import pytest

from day04 import is_passphrase_valid


@pytest.mark.parametrize("passphrase, is_valid", [
    ("aa bb cc dd ee", True),
    ("aa bb cc dd ee aa", False),
    ("aa bb cc dd ee aaa", True),
])
def test_is_passphrase_valid_with_default_transform(passphrase: str, is_valid: bool):
    assert is_valid == is_passphrase_valid(passphrase, lambda word: word)


@pytest.mark.parametrize("passphrase, is_valid", [
    ("abcde fghij", True),
    ("abcde xyz ecdab", False),
    ("a ab abc abd abf abj", True),
    ("iiii oiii ooii oooi oooo", True),
    ("oiii ioii iioi iiio", False),
])
def test_is_passphrase_valid_with_sorted_transform(passphrase: str, is_valid: bool):
    assert is_valid == is_passphrase_valid(passphrase, lambda word: str(sorted(word)))
