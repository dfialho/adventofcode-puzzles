import operator
from functools import reduce
from typing import Iterator, List, Iterable


def slide(elements: List[int], offset: int) -> List[int]:
    bound = offset % len(elements)
    return elements[bound:] + elements[:bound]


def reverse(elements: List[int], length: int) -> List[int]:
    elements[:length] = reversed(elements[:length])
    return elements


def xor(iterable: Iterable[int]) -> int:
    return reduce(operator.xor, iterable)


def hash_round(elements: List[int], lengths: Iterator[int], position: int, skip_size: int):
    for length in lengths:
        elements = reverse(elements, length)
        elements = slide(elements, length + skip_size)
        position = (position + length + skip_size) % len(elements)
        skip_size += 1

    return elements, position, skip_size


def hex_str(value: int) -> str:
    return f'{value:0{2}x}'


def knot_hash(input_str: str) -> str:
    # Convert characters to their ascii codes
    lengths = [ord(character) for character in input_str]
    # Append fixed suffix
    lengths.extend([17, 31, 73, 47, 23])

    position, skip_size = 0, 0
    elements = [i for i in range(256)]

    # Compute sparse hash
    for i in range(64):
        elements, position, skip_size = hash_round(elements, lengths, position, skip_size)

    # Adjust the elements to their expected positions
    elements = slide(elements, -position)

    # Compute dense hash
    dense_hash = [xor(elements[i * 16:i * 16 + 16]) for i in range(256 // 16)]

    # Convert to hexadecimal string
    hash_str = "".join(hex_str(value) for value in dense_hash)
    return hash_str


def input(path: str) -> str:
    with open(path) as file:
        return file.read()


def main():
    print("Solution part 2:", knot_hash(input("input.txt")))


if __name__ == '__main__':
    main()
