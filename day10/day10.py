import operator
from functools import reduce
from typing import Iterator, List, Iterable


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


def input(path: str) -> str:
    with open(path) as file:
        return file.read()


def lengths_from(input_str) -> Iterator[int]:
    for value in input_str.split(','):
        yield int(value)


def main():
    #
    # Part 1
    #

    sparse_hash = hash_rounds(lengths_from(input("input.txt")), [i for i in range(256)], count=1)
    print("Solution part 1:", sparse_hash[0] * sparse_hash[1])

    #
    # Part 2
    #

    print("Solution part 2:", knot_hash(input("input.txt")))


if __name__ == '__main__':
    main()
