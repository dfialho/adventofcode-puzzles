from typing import Tuple, List, Iterator, NamedTuple, Dict


class Program(NamedTuple):
    name: str
    weight: int
    sub_programs: List['Program'] = []

    def __eq__(self, other: 'Program') -> bool:
        return self.name == other.name

    def __hash__(self) -> int:
        return hash(self.name)


def tower_weight(program: Program) -> int:
    weight = program.weight

    weight_to_program = {}
    sub_weights = []
    for sub_program in program.sub_programs:
        sub_tower_weight = tower_weight(sub_program)
        weight_to_program[sub_tower_weight] = sub_program
        sub_weights.append(sub_tower_weight)

    if sub_weights:
        different_weight, common_weight = find_different(sub_weights)

        if different_weight != common_weight:
            sub_program = weight_to_program[different_weight]
            print("SOLUTION:", common_weight - different_weight + sub_program.weight)

    return weight + sum(sub_weights)


def find_different(values: List[int]) -> Tuple[int, int]:
    """
    Looks for a value that is different among a list of *values* that are almost all equal to
    each other. It returns the different value and the common value. If all values are equal,
    then it returns two equal values.

    It assumes that most values are equal with the exception of only one.
    It also assumes the list of values has at least 3 values.

    :return: tuple with the value different from all the others and the common value.
    """
    if values.count(max(values)) == 1:
        return max(values), min(values)
    else:
        return min(values), max(values)


def build_tower(programs: Iterator[Tuple[str, int, List[str]]]) -> Program:
    """
    Builds the tower of programs.

    :return: the program at the bottom of the tower
    """
    # Dictionary to map program names to actual programs
    program_by_name: Dict[str, Program] = {}
    # Stores a list of pairs. Each pair holds a program name and the name of one of its sub-programs
    sub_programs_names: List[Tuple[str, str]] = []

    # Initialize 'program_by_name' and 'sub_programs_names' based on the input
    for name, weight, sub_names in programs:
        program_by_name[name] = Program(name, weight, [])
        sub_programs_names.extend((name, sub_name) for sub_name in sub_names)

    # Add the actual sub-programs to each program according to 'sub_programs_by_name'
    for name, sub_name in sub_programs_names:
        program_by_name[name].sub_programs.append(program_by_name[sub_name])

    # If the input is correct the result of this difference should contain a single program,
    # the bottom program
    bottom_program = set(program_by_name) - set(sub_name for _, sub_name in sub_programs_names)
    return program_by_name[bottom_program.pop()]


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
    tower_weight(build_tower(programs("input.txt")))


if __name__ == '__main__':
    main()
