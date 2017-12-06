import operator
from typing import List, Set, Tuple


def read_configuration(path: str) -> List[int]:
    with open(path) as file:
        return list(map(int, file.read().split('\t')))


def count_cycles(configuration: List[int]) -> int:
    bank_count = len(configuration)
    current_configuration = tuple(configuration)
    past_configurations: Set[tuple] = set()
    cycle_count = 0

    while current_configuration not in past_configurations:
        past_configurations.add(current_configuration)

        bank, block_count = max_and_index(configuration)

        # Clear the bank
        configuration[bank] = 0

        # Redistribute the blocks among all banks
        for i in range(block_count):
            configuration[(bank + i + 1) % bank_count] += 1

        cycle_count += 1
        current_configuration = tuple(configuration)

    return cycle_count


def max_and_index(values: List[int]) -> Tuple[int, int]:
    """ Returns the max value and the corresponding index """
    max_index, max_value = max(enumerate(values), key=operator.itemgetter(1))
    return max_index, max_value


def main() -> None:
    print("Solution part 1:", count_cycles(read_configuration("input.txt")))


if __name__ == '__main__':
    main()
