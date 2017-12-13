from typing import Dict


def calculate_severity(layers: Dict[int, int]) -> int:
    severity = 0
    for depth, range in layers.items():
        if depth % (2 * (range - 1)) == 0:
            severity += depth * range

    return severity


def input(path: str) -> Dict[int, int]:
    with open(path) as file:
        layers: Dict[int, int] = {}
        for line in file:
            depth, range = map(int, line.split(":"))
            layers[depth] = range

    return layers


def main():
    #
    # Part 1
    #

    print("Solution part 1:", calculate_severity(input("input.txt")))

    #
    # Part 2
    #


if __name__ == '__main__':
    main()
