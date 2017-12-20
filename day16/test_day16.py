from typing import List

import pytest

from day16 import SpinMove, ExchangeMove, PartnerMove


@pytest.mark.parametrize("programs, size, output", [
    (['a', 'b', 'c', 'd', 'e'], 3, ['c', 'd', 'e', 'a', 'b']),
    (['a', 'b', 'c', 'd', 'e'], 1, ['e', 'a', 'b', 'c', 'd']),
    (['a', 'b', 'c', 'd', 'e'], 0, ['a', 'b', 'c', 'd', 'e']),
    (['a', 'b', 'c', 'd', 'e'], 2, ['d', 'e', 'a', 'b', 'c']),
    (['a', 'b', 'c', 'd', 'e'], 4, ['b', 'c', 'd', 'e', 'a']),
    (['a', 'b', 'c', 'd', 'e'], 5, ['a', 'b', 'c', 'd', 'e']),
])
def test_spin_move(programs: List[str], size: int, output: List[str]):
    assert output == SpinMove(size).do(programs)


@pytest.mark.parametrize("programs, position_a, position_b, output", [
    (['a', 'b', 'c', 'd', 'e'], 0, 0, ['a', 'b', 'c', 'd', 'e']),
    (['a', 'b', 'c', 'd', 'e'], 0, 1, ['b', 'a', 'c', 'd', 'e']),
    (['a', 'b', 'c', 'd', 'e'], 0, 4, ['e', 'b', 'c', 'd', 'a']),
    (['a', 'b', 'c', 'd', 'e'], 3, 4, ['a', 'b', 'c', 'e', 'd']),
    (['a', 'b', 'c', 'd', 'e'], 4, 2, ['a', 'b', 'e', 'd', 'c']),
])
def test_exchange_move(programs: List[str], position_a: int, position_b: int, output: List[str]):
    assert output == ExchangeMove(position_a, position_b).do(programs)


@pytest.mark.parametrize("programs, program_a, program_b, output", [
    (['a', 'b', 'c', 'd', 'e'], 'a', 'a', ['a', 'b', 'c', 'd', 'e']),
    (['a', 'b', 'c', 'd', 'e'], 'a', 'b', ['b', 'a', 'c', 'd', 'e']),
    (['a', 'b', 'c', 'd', 'e'], 'b', 'a', ['b', 'a', 'c', 'd', 'e']),
    (['a', 'b', 'c', 'd', 'e'], 'a', 'e', ['e', 'b', 'c', 'd', 'a']),
    (['a', 'b', 'c', 'd', 'e'], 'd', 'e', ['a', 'b', 'c', 'e', 'd']),
    (['a', 'b', 'c', 'd', 'e'], 'e', 'c', ['a', 'b', 'e', 'd', 'c']),
])
def test_partner_move(programs: List[str], program_a: str, program_b: str, output: List[str]):
    assert output == PartnerMove(program_a, program_b).do(programs)
