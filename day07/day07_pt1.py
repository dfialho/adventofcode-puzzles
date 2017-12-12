from typing import Tuple, List, Iterator, Set


def find_bottom_program(programs: Iterator[Tuple[str, List[str]]]) -> str:
    all_programs: Set[str] = set()
    all_sub_programs: Set[str] = set()

    for program, sub_programs in programs:
        all_programs.add(program)
        all_sub_programs.update(sub_programs)

    # If the input is correct the result of this difference should contain a single program,
    # the bottom program
    bottom_program = all_programs - all_sub_programs
    return bottom_program.pop()


def input(path: str) -> Iterator[Tuple[str, List[str]]]:
    with open(path) as file:
        for line in file:
            program, *sub_programs = line.split("->")
            name, _ = program.strip().split(" ")

            if sub_programs:
                sub_programs = [sub_program.strip() for sub_program in sub_programs[0].split(", ")]

            yield name, sub_programs


def main():
    print("Solution part 1:", find_bottom_program(input("input.txt")))


if __name__ == '__main__':
    main()
