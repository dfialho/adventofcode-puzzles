import operator
from typing import List, Set, Tuple


def read_configuration(path: str) -> List[int]:
    with open(path) as file:
        return list(map(int, file.read().split('\t')))


def loop_size(configuration: List[int]) -> int:
    bank_count = len(configuration)
    past_configurations: List[tuple] = []
    current_configuration = tuple(configuration)
    cycle_count = 0

    while current_configuration not in past_configurations:
        past_configurations.append(current_configuration)

        # Find the bank with the highest number of blocks
        bank, block_count = max(enumerate(configuration), key=operator.itemgetter(1))

        # Clear the bank and redistribute its blocks among all banks
        configuration[bank] = 0
        for i in range(block_count):
            configuration[(bank + i + 1) % bank_count] += 1

        cycle_count += 1
        current_configuration = tuple(configuration)

    return cycle_count - past_configurations.index(current_configuration)


def main() -> None:
    print("Solution part 2:", loop_size(read_configuration("input.txt")))


if __name__ == '__main__':
    main()
