from typing import Tuple, List, Iterator, Set, NamedTuple, Dict

import sys


class Program(NamedTuple):
    name: str
    weight: int
    sub_programs: List['Program'] = []

    def __eq__(self, other: 'Program') -> bool:
        return self.name == other.name

    def __hash__(self) -> int:
        return hash(self.name)


def find_odd(values: List[int]) -> Tuple[int, int]:
    if values.count(max(values)) == 1:
        return max(values), min(values)
    else:
        return min(values), max(values)


def tower_weight(program: Program) -> int:
    weight = program.weight

    weight_to_program = {}
    sub_weights = []
    for sub_program in program.sub_programs:
        sub_tower_weight = tower_weight(sub_program)
        weight_to_program[sub_tower_weight] = sub_program
        sub_weights.append(sub_tower_weight)

    if sub_weights:
        different_weight, common_weight = find_odd(sub_weights)

        if different_weight != common_weight:
            sub_program = weight_to_program[different_weight]
            print("SOLUTION:", common_weight - different_weight + sub_program.weight)

    return weight + sum(sub_weights)


def read_tree(programs: Iterator[Tuple[str, int, List[str]]]) -> Program:
    # Stores all programs found in the input
    all_programs: List[Program] = []
    # Dictionary to map program names to actual programs
    program_by_name: Dict[str, Program] = {}
    # Stores a list of sub-program names for each program
    sub_programs_by_name: Dict[str, List[str]] = {}

    for name, weight, sub_programs in programs:
        program = Program(name, weight, [])
        all_programs.append(program)
        program_by_name[name] = program
        sub_programs_by_name[name] = sub_programs

    # Add the actual sub-programs to each program according to 'sub_programs_by_name'
    for program in all_programs:
        for sub_program in sub_programs_by_name[program.name]:
            program.sub_programs.append(program_by_name[sub_program])

    return find_bottom_program(all_programs)


def find_bottom_program(programs: Iterator[Program]) -> Program:
    # Put all sub-programs in a set
    sub_programs = set(sub_program for program in programs for sub_program in program.sub_programs)

    # If the input is correct the result of this difference should contain a single program,
    # the bottom program
    bottom_program = set(programs) - sub_programs
    return bottom_program.pop()


def programs(path: str) -> Iterator[Tuple[str, int, List[str]]]:
    """
    Parses each line in the input. A line is converted to a tuple containing (1) the program name,
    (2) the program weight, and (3) a list with the names of the sub-programs. This list is empty
    if the program has no sub_programs.

    :return: tuple with the program name, weight, an list of sub-programs' names
    """
    with open(path) as file:
        for line in file:
            program_attributes, *sub_programs = line.split("->")
            name, weight = program_attributes.strip().split(" ")

            # Remove parenthesis and convert to integer
            weight = int(weight[1:-1])

            if sub_programs:
                sub_programs = [sub_program.strip() for sub_program in sub_programs[0].split(", ")]

            yield name, weight, sub_programs


def main():
    tower_weight(read_tree(programs("input_example.txt")))


if __name__ == '__main__':
    main()
