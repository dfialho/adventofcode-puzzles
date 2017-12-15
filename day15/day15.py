from typing import Tuple, Iterator


def judge(generator_a: Iterator[int], generator_b: Iterator[int], n_pairs: int):
    count = 0
    for i in range(n_pairs):
        if next(generator_a) & 0xFFFF == next(generator_b) & 0xFFFF:
            count += 1

    return count


def generator(seed: int, factor: int, multiple: int = 1) -> Iterator[int]:
    value = seed
    while True:
        value = (value * factor) % 2147483647
        if value % multiple == 0:
            yield value


def input(path: str) -> Tuple[int, int]:
    with open(path) as file:
        seed_a = int(file.readline().replace("Generator A starts with ", ""))
        seed_b = int(file.readline().replace("Generator B starts with ", ""))
        return seed_a, seed_b


def main():
    #
    # Part 1
    #
    seed_a, seed_b = input("input.txt")
    print("Solution part 1:", judge(
        generator_a=generator(seed_a, factor=16807),
        generator_b=generator(seed_b, factor=48271),
        n_pairs=40000000
    ))

    #
    # Part 2
    #
    seed_a, seed_b = input("input.txt")
    print("Solution part 2:", judge(
        generator_a=generator(seed_a, factor=16807, multiple=4),
        generator_b=generator(seed_b, factor=48271, multiple=8),
        n_pairs=5000000
    ))


if __name__ == '__main__':
    main()
