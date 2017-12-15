from typing import Tuple


def judge(seed_a: int, factor_a: int, seed_b: int, factor_b: int):
    value_a = seed_a
    value_b = seed_b

    count = 0
    for i in range(40000000):
        value_a = (value_a * factor_a) % 2147483647
        value_b = (value_b * factor_b) % 2147483647

        if value_a & 0xFFFF == value_b & 0xFFFF:
            count += 1

    return count


def picky_judge(seed_a: int, factor_a: int, seed_b: int, factor_b: int):
    value_a = seed_a
    value_b = seed_b

    count = 0
    for i in range(5000000):
        value_a = (value_a * factor_a) % 2147483647
        while value_a & 0x03 != 0:
            value_a = (value_a * factor_a) % 2147483647

        value_b = (value_b * factor_b) % 2147483647
        while value_b & 0x07 != 0:
            value_b = (value_b * factor_b) % 2147483647

        if value_a & 0xFFFF == value_b & 0xFFFF:
            count += 1

    return count


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
    print("Solution part 1:", judge(seed_a, 16807, seed_b, 48271))
    print("Solution part 2:", picky_judge(seed_a, 16807, seed_b, 48271))


if __name__ == '__main__':
    main()
