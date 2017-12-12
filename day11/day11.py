from typing import Iterator, NamedTuple


class Position(NamedTuple):
    x: int
    y: int
    z: int

    @property
    def distance(self) -> int:
        x, y, z = abs(self.x), abs(self.y), abs(self.z)
        return max(x, y, z)


class Direction(NamedTuple):
    x: int
    y: int
    z: int


directions = {
    'n': Direction(-1, 1, 0),
    'ne': Direction(0, 1, -1),
    'se': Direction(1, 0, -1),
    's': Direction(1, -1, 0),
    'sw': Direction(0, -1, 1),
    'nw': Direction(-1, 0, 1),
}


def move(position: Position, direction: Direction) -> Position:
    return Position(
        x=position.x + direction.x,
        y=position.y + direction.y,
        z=position.z + direction.z,
    )


def child_positions(steps: Iterator[str]) -> Iterator[Position]:
    position = Position(0, 0, 0)
    yield position

    for step in steps:
        position = move(position, directions[step])
        yield position


def child_position(steps: Iterator[str]) -> Position:
    position = Position(0, 0, 0)
    for position in child_positions(steps):
        pass

    return position


def input(path: str) -> Iterator[str]:
    with open(path) as file:
        for direction in file.read().split(','):
            yield direction


def main():
    #
    # Part 1
    #

    print("Solution part 1:", child_position(input("input.txt")).distance)

    #
    # Part 2
    #

    furthest_position = max(child_positions(input("input.txt")), key=lambda p: p.distance)
    print("Solution part 2:", furthest_position.distance)


if __name__ == '__main__':
    main()
