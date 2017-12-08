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


def find_odd(values: list) -> (int, int):
    if max(values) != min(values):
        if values.count(max(values)) == 1:
            return max(values), min(values)
        else:
            return min(values), max(values)

    return values[0], values[0]


def tower_weight(program: Program) -> int:
    weight = program.weight
    sub_weights = [(sub_program, tower_weight(sub_program)) for sub_program in program.sub_programs]

    if sub_weights:
        odd_value, normal_value = find_odd([w for p, w in sub_weights])

        if odd_value != normal_value:
            for sub_program, sub_weight in sub_weights:
                if odd_value == sub_weight:
                    print("SOLUTION:", normal_value - odd_value + sub_program.weight)
                    sys.exit(1)

    # print(f"{program.name}: {weight}")
    return weight + sum(w for p, w in sub_weights)


def read_tree(programs: Iterator[Tuple[str, int, List[str]]]) -> Program:
    all_programs: Dict[str, Program] = {}
    all_sub_programs: Dict[str, List[str]] = {}

    for name, weight, sub_programs in programs:
        all_programs[name] = Program(name, weight, [])
        all_sub_programs[name] = sub_programs

    for program in all_programs.values():
        for sub_program in all_sub_programs[program.name]:
            program.sub_programs.append(all_programs[sub_program])

    return all_programs[find_bottom_program(iter(all_programs.values()))]


def find_bottom_program(programs: Iterator[Program]) -> str:
    all_programs: Set[str] = set()
    all_sub_programs: Set[str] = set()

    for program in programs:
        all_programs.add(program.name)
        all_sub_programs.update([sub_program.name for sub_program in program.sub_programs])

    # If the input is correct the result of this difference should contain a single program,
    # the bottom program
    bottom_program = all_programs - all_sub_programs
    return bottom_program.pop()


def programs(path: str) -> Iterator[Tuple[str, int, List[str]]]:
    with open(path) as file:
        for line in file:
            program_params, *sub_programs = line.split("->")
            name, weight = program_params.strip().split(" ")

            # Remove parenthesis
            weight = int(weight[1:-1])

            if sub_programs:
                sub_programs = [sub_program.strip() for sub_program in sub_programs[0].split(", ")]

            yield name, weight, sub_programs


def main():
    tower_weight(read_tree(programs("input.txt")))


if __name__ == '__main__':
    main()
