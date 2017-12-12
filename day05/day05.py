from typing import Callable, List, Iterator


def count_steps(offsets: List[int], offset_adjustment: Callable[[int], int]) -> int:
    current_position = 0
    step_count = 0
    offset_count = len(offsets)

    while 0 <= current_position < offset_count:
        offset = offsets[current_position]
        offsets[current_position] += offset_adjustment(offset)
        current_position += offset
        step_count += 1

    return step_count


def input(path: str) -> Iterator[int]:
    with open(path) as file:
        for line in file:
            yield int(line)


def main() -> None:
    print("Solution part 1:", count_steps(list(input("input.txt")), lambda offset: 1))
    print("Solution part 2:", count_steps(list(input("input.txt")),
                                          lambda offset: -1 if offset >= 3 else +1))


if __name__ == '__main__':
    main()
