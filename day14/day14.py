import random
from typing import List, Iterator

import hashing


def hashes(key: str, n: int) -> Iterator[str]:
    for i in range(n):
        yield hashing.knot_hash(f"{key}-{i}")


def to_bits(hash_str: str) -> str:
    return "".join(f"{int(character, 16):04b}" for character in hash_str)


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

    for i in range(5):
        value = random.randint(1, 16)
        print(f"{value:05b}")


if __name__ == '__main__':
    main()
