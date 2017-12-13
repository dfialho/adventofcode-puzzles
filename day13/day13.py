from typing import Iterator, List, Tuple


def is_caught(time: int, height: int):
    return time % (2 * (height - 1)) == 0


def calculate_delay(layers: List[Tuple[int, int]]) -> int:
    delay = -1
    caught = True

    while caught:
        delay += 1
        caught = False

        for depth, height in layers:
            if is_caught(depth + delay, height):
                caught = True
                break

    return delay


def calculate_severity(layers: List[Tuple[int, int]]) -> int:
    severity = 0
    for depth, height in layers:
        if is_caught(depth, height):
            severity += depth * height

    return severity


def input(path: str) -> Iterator[Tuple[int, int]]:
    with open(path) as file:
        for line in file:
            depth, height = map(int, line.split(":"))
            yield depth, height


def main():
    #
    # Part 1
    #
    print("Solution part 1:", calculate_severity(list(input("input.txt"))))

    #
    # Part 2
    #
    print("Solution part 2:", calculate_delay(list(input("input.txt"))))


if __name__ == '__main__':
    main()
