from typing import List, Iterator, Dict, Tuple, NewType, Optional

import hashing


def hashes(key: str, n: int) -> Iterator[str]:
    for i in range(n):
        yield hashing.knot_hash(f"{key}-{i}")


def to_bits(hash_str: str) -> str:
    return "".join(f"{int(character, 16):04b}" for character in hash_str)


Position = NewType('Position', Tuple[int, int])
Group = NewType('Group', int)


class Grid:

    def __init__(self, size: int):
        self._groups: List[List[int]] = [[None] * size for i in range(size)]

    def __getitem__(self, position: Position):
        x, y = position

        if x >= 128 or x < 0 or y >= 128 or y < 0:
            return None

        return self._groups[y][x]

    def __setitem__(self, position: Position, value: int):
        x, y = position
        self._groups[y][x] = value


def min_optional(a: Optional[int], b: Optional[int]) -> Optional[int]:
    if a is None:
        return b
    elif b is None:
        return a
    else:
        return min(a, b)


def count_groups(key: str) -> int:
    groups: Dict[Group, List[Position]] = {}
    group_grid = Grid(size=128)
    next_group = 1

    for y, hash_str in enumerate(hashes(key, n=128)):
        for x, bit in enumerate(to_bits(hash_str)):
            if bit == '0':
                continue

            left = group_grid[x - 1, y]
            top = group_grid[x, y - 1]

            if not left and not top:
                # This is a new group
                group_grid[x, y] = next_group
                groups[next_group] = [(x, y)]
                next_group += 1

            else:
                group = min_optional(left, top)
                group_grid[x, y] = group
                groups[group].append((x, y))

                if left and top and left != top:
                    # All positions in group with highest ID need to moved to group with lowest ID
                    lowest_group = min(left, top)
                    highest_group = max(left, top)

                    for position in groups[highest_group]:
                        group_grid[position] = lowest_group
                        groups[lowest_group].append(position)
                    del groups[highest_group]

    return len(groups)


def build_grid(key: str) -> List[str]:
    return [to_bits(hash_str) for hash_str in hashes(key, n=128)]


def count_used(grid: List[str]) -> int:
    return sum(row.count('1') for row in grid)


def input(path: str) -> str:
    with open(path) as file:
        return file.read()


def main():
    #
    # Part 1
    #
    print("Solution part 1:", count_used(build_grid(input("input.txt"))))

    #
    # Part 2
    #
    print("Solution part 1:", count_groups(input("input.txt")))


if __name__ == '__main__':
    main()
