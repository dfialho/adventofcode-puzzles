from functools import reduce
from typing import Iterable, List

import operator


def slide(elements: List[int], offset: int) -> List[int]:
    offset %= len(elements)
    return elements[offset:] + elements[:offset]


def reverse(elements: List[int], length: int) -> List[int]:
    elements[:length] = reversed(elements[:length])
    return elements


def xor(iterable: Iterable[int]) -> int:
    return reduce(operator.xor, iterable)


def hex_str(value: int) -> str:
    return f'{value:0{2}x}'


def hash_rounds(lengths: Iterable[int], elements: List[int], count: int = 1):
    position, skip_size = 0, 0
    for i in range(count):
        for length in lengths:
            elements = reverse(elements, length)
            elements = slide(elements, length + skip_size)
            position = (position + length + skip_size) % len(elements)
            skip_size += 1

    # Adjust the elements to their expected positions
    return slide(elements, -position)


def knot_hash(input_str: str) -> str:
    # Convert characters to their ascii codes
    lengths = [ord(character) for character in input_str]

    # Append fixed suffix
    lengths.extend([17, 31, 73, 47, 23])

    # Compute sparse hash
    sparse_hash = hash_rounds(lengths, elements=[i for i in range(256)], count=64)

    # Compute dense hash
    dense_hash = [xor(sparse_hash[i * 16:i * 16 + 16]) for i in range(256 // 16)]

    # Convert to hexadecimal string
    hash_str = "".join(hex_str(value) for value in dense_hash)
    return hash_str
