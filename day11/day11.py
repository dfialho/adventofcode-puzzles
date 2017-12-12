from typing import Iterator, NamedTuple, NewType, Tuple


class Position(NamedTuple):
    x: int
    y: int
    z: int


class Direction(NamedTuple):
    x: int
    y: int
    z: int


def move(position: Position, direction: Direction) -> Position:
    return Position(
        x=position.x + direction.x,
        y=position.y + direction.y,
        z=position.z + direction.z,
    )


directions = {
    'n': Direction(-1, 1, 0),
    'ne': Direction(0, 1, -1),
    'se': Direction(1, 0, -1),
    's': Direction(1, -1, 0),
    'sw': Direction(0, -1, 1),
    'nw': Direction(-1, 0, 1),
}


def child_position(steps: Iterator[str]) -> Position:
    position = Position(0, 0, 0)
    for step in steps:
        position = move(position, directions[step])

    return position


def min_steps(position: Position) -> int:
    x, y, z = abs(position.x), abs(position.y), abs(position.z)
    return max(x, y, z)


def input(path: str) -> Iterator[str]:
    with open(path) as file:
        for direction in file.read().split(','):
            yield direction


def main():
    #
    # Part 1
    #

    print("Solution part 1:", min_steps(child_position(input("input.txt"))))

    #
    # Part 2
    #



if __name__ == '__main__':
    main()
