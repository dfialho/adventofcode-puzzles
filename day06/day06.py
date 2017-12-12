from typing import List, Iterator, Tuple

import operator


def count_cycles(configuration: List[int]) -> Tuple[int, int]:
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

    return cycle_count, cycle_count - past_configurations.index(current_configuration)


def input(path: str) -> Iterator[int]:
    with open(path) as file:
        return map(int, file.read().split('\t'))


def main() -> None:
    redistribution_cycle_count, loop_size = count_cycles(list(input("input.txt")))
    print("Solution part 1:", redistribution_cycle_count)
    print("Solution part 2:", loop_size)


if __name__ == '__main__':
    main()
