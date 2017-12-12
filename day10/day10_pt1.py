from typing import Iterator, List


def slide(elements: List[int], offset: int) -> List[int]:
    bound = offset % len(elements)
    return elements[bound:] + elements[:bound]


def reverse(elements: List[int], length: int) -> List[int]:
    elements[:length] = reversed(elements[:length])
    return elements


def knot_hash(element_count: int, lengths: Iterator[int]) -> int:
    elements = [i for i in range(element_count)]
    position = 0
    for skip_size, length in enumerate(lengths):
        elements = reverse(elements, length)
        elements = slide(elements, length + skip_size)
        position = (position + length + skip_size) % element_count

    # Adjust the elements to their expected positions
    elements = slide(elements, -position)

    return elements[0] * elements[1]


def lengths(path: str) -> Iterator[int]:
    with open(path) as file:
        for value in file.read().split(','):
            yield int(value)


def main():
    print("Solution part 1:", knot_hash(256, lengths("input.txt")))
    # print("Solution part 1:", knot_hash(5, lengths("input_example.txt")))


if __name__ == '__main__':
    main()
