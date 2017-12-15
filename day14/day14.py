from typing import List, Iterator, Dict, Tuple, NewType, Optional

import hashing


def hashes(key: str, n: int) -> Iterator[str]:
    """ Generates the *n* hash strings for the given *key* """
    for i in range(n):
        yield hashing.knot_hash(f"{key}-{i}")


def bits(hash_str: str) -> Iterator[str]:
    """ Generates each bit in the given hash string *hash_str* """
    for character in hash_str:
        for bit in f"{int(character, 16):04b}":
            yield bit


Position = NewType('Position', Tuple[int, int])


class Grid:
    """ Square grid (NxN) to hold integer values """

    def __init__(self, size: int):
        """
        Initializes a square grid with dimensions (size x size). All positions of the grid are
        set to None.
        """
        self._groups: List[List[int]] = [[None] * size for i in range(size)]

    def __getitem__(self, position: Position) -> Optional[int]:
        """
        Gets the value in the given *position* of the grid. It returns None if the
        given *position* is outside of the grid.
        """
        x, y = position

        if x >= 128 or x < 0 or y >= 128 or y < 0:
            return None

        return self._groups[y][x]

    def __setitem__(self, position: Position, value: int):
        """ Sets the *value* for the specified *position* """
        x, y = position
        self._groups[y][x] = value


def min_optional(a: Optional[int], b: Optional[int]) -> Optional[int]:
    """
    Returns the minimum between two optional integers. It works in the same way as the 'min'
    built-in function, except that it supports None values. A None value is always considered
    higher than a no-None value.
    """
    if a is None:
        return b
    elif b is None:
        return a
    else:
        return min(a, b)


def count_regions(key: str) -> int:
    # Stores the positions belonging to each group
    regions: Dict[int, List[Position]] = {}
    # Grid holding the regions IDs of each position
    region_grid = Grid(size=128)
    # Stores an ID to assign to each new region found
    next_region_id = 1

    for y, hash_str in enumerate(hashes(key, n=128)):
        for x, bit in enumerate(bits(hash_str)):
            if bit == '0':
                # ignore free bits
                continue

            left_region = region_grid[x - 1, y]
            top_region = region_grid[x, y - 1]

            if not left_region and not top_region:
                # This bit starts a new region
                regions[next_region_id] = [(x, y)]
                region_grid[x, y] = next_region_id
                next_region_id += 1

            else:
                # This position either belongs to the top or left region
                # It belongs to the one with the lowest ID
                region = min_optional(left_region, top_region)

                # Set region for this position
                regions[region].append((x, y))
                region_grid[x, y] = region

                # If the left and top regions are not the same, then this two regions are now the
                # same. Therefore, all positions in this two regions need to be set to the same
                # region
                if left_region and top_region and left_region != top_region:
                    lowest_group = min(left_region, top_region)
                    highest_group = max(left_region, top_region)

                    # Move all positions in the region with the highest ID to the one with the
                    # lowest ID
                    for position in regions[highest_group]:
                        regions[lowest_group].append(position)
                        region_grid[position] = lowest_group

                    # The region with the highest ID no longer exists
                    del regions[highest_group]

    return len(regions)


def count_used(key: str) -> int:
    return sum(1 for hash_str in hashes(key, n=128) for bit in bits(hash_str) if bit == '1')


def input(path: str) -> str:
    with open(path) as file:
        return file.read()


def main():
    #
    # Part 1
    #
    print("Solution part 1:", count_used(input("input.txt")))

    #
    # Part 2
    #
    print("Solution part 2:", count_regions(input("input.txt")))


if __name__ == '__main__':
    main()
