from typing import Generator, Tuple, List, Iterator, NamedTuple, Set


class Program(NamedTuple):
    name: str
    sub_programs: List[str]


def find_bottom_program(programs: Iterator[Program]) -> str:
    all_programs: Set[str] = set()
    all_sub_programs: Set[str] = set()

    for program in programs:
        all_programs.add(program.name)
        all_sub_programs.update(program.sub_programs)

    bottom_program = all_programs - all_sub_programs
    return bottom_program.pop()


def programs(path: str) -> Generator[Program, None, None]:
    with open(path) as file:
        for line in file:
            if "->" in line:
                program_params, sub_programs = line.split("->")
                name, weight = program_params.strip().split(" ")
                sub_programs = [sub_program.strip() for sub_program in sub_programs.split(",")]
            else:
                name, weight = line.strip().split(" ")
                sub_programs = []

            yield Program(name, sub_programs)


def main():
    print("Solution part 1:", find_bottom_program(programs("input.txt")))


if __name__ == '__main__':
    main()
