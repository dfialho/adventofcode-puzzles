from typing import Tuple, Iterator


def judge(generator_a: Iterator[int], generator_b: Iterator[int]):
    count = 0
    for i in range(40000000):
        if next(generator_a) & 0xFFFF == next(generator_b) & 0xFFFF:
            count += 1

    return count


def generator(seed: int, factor: int) -> Iterator[int]:
    value = seed
    while True:
        value = (value * factor) % 2147483647
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
        generator(seed_a, factor=16807),
        generator(seed_b, factor=48271)
    ))


if __name__ == '__main__':
    main()
