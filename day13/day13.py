from typing import Iterator, List, Tuple


def calculate_delay(layers: List[Tuple[int, int]]) -> int:
    delay = -1
    caught = True

    while caught:
        delay += 1
        caught = False

        for depth, height in layers:
            if (depth + delay) % (2 * (height - 1)) == 0:
                caught = True
                break

    return delay


def calculate_severity(layers: List[Tuple[int, int]]) -> int:
    severity = 0
    for depth, height in layers:
        if depth % (2 * (height - 1)) == 0:
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
