from typing import Iterator, List

from abc import ABC, abstractmethod


class DanceMove(ABC):

    @abstractmethod
    def do(self, programs: List[str]) -> List[str]:
        pass


class SpinMove(DanceMove):

    def __init__(self, size: int):
        self.size = size

    def do(self, programs: List[str]) -> List[str]:
        return programs[-self.size:] + programs[:-self.size]


class ExchangeMove(DanceMove):

    def __init__(self, a: int, b: int):
        self.a = a
        self.b = b

    def do(self, programs: List[str]) -> List[str]:
        programs[self.a], programs[self.b] = programs[self.b], programs[self.a]
        return programs


class PartnerMove(DanceMove):

    def __init__(self, a: str, program_b: str):
        self.a = a
        self.b = program_b

    def do(self, programs: List[str]) -> List[str]:
        position_a = programs.index(self.a)
        position_b = programs.index(self.b)
        programs[position_a] = self.b
        programs[position_b] = self.a
        return programs


def dance_moves(tokens: Iterator[str]) -> Iterator[DanceMove]:
    for token in tokens:
        move_label = token[0]
        move_params = token[1:]

        if move_label == 's':
            move = SpinMove(size=int(move_params))
        elif move_label == 'x':
            position_a, position_b = map(int, move_params.split("/"))
            move = ExchangeMove(position_a, position_b)
        elif move_label == 'p':
            program_a, program_b = move_params.split("/")
            move = PartnerMove(program_a, program_b)
        else:
            raise ValueError(f"invalid toke: {token}")

        yield move


def dance(moves: Iterator[DanceMove], n: int = 1) -> List[str]:
    programs = [chr(ord('a') + i) for i in range(16)]

    moves = list(moves)
    for i in range(n):
        for move in moves:
            programs = move.do(programs)

    return programs


def input(path: str) -> Iterator[str]:
    with open(path) as file:
        for token in file.read().split(","):
            yield token


def main():
    #
    # Part 1
    #
    print("Solution part 1:", "".join(dance(dance_moves(input("input.txt")))))

    #
    # Part 2
    #
    print("Solution part 2:", "".join(dance(dance_moves(input("input.txt")), n=1000000000)))


if __name__ == '__main__':
    main()
