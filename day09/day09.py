from typing import Iterator, Tuple


class ParseError(Exception):
    pass


class Parser:

    def __init__(self):
        self.stack_count = 0
        self.state = None
        self.score = 0
        self.garbage_count = 0

    def parse(self, stream: Iterator[str]) -> Tuple[int, int]:

        character = next(stream)

        if character != '{':
            raise ParseError()

        self.begin_group()
        self.state = self.group_state

        while self.stack_count > 0:
            character = next(stream)
            self.state(character)

        return self.score, self.garbage_count

    def group_state(self, character: str):

        if character == '{':
            self.begin_group()
        elif character == '<':
            self.state = self.garbage_state
        elif character == '}':
            self.end_group()
            self.state = self.end_group_state
        else:
            raise ParseError()

    def end_group_state(self, character: str):

        if character == '}':
            self.end_group()
        elif character == ',':
            self.state = self.group_state
        else:
            raise ParseError()

    def garbage_state(self, character: str):

        if character == '!':
            self.state = self.ignore_state
        elif character == '>':
            self.state = self.end_garbage_state
        else:
            self.garbage_count += 1

    def end_garbage_state(self, character: str):

        if character == ',':
            self.state = self.group_state
        elif character == '}':
            self.end_group()
            self.state = self.end_group_state
        else:
            raise ParseError()

    def ignore_state(self, character: str):
        self.state = self.garbage_state

    def begin_group(self):
        self.stack_count += 1

    def end_group(self):
        self.score += self.stack_count
        self.stack_count -= 1

        if self.stack_count < 0:
            raise ParseError()


def streamer(path: str) -> Iterator[str]:
    with open(path) as file:
        return iter(file.read())


def main():
    solution_1, solution_2 = Parser().parse(streamer("input.txt"))
    print("Solution part 1:", solution_1)
    print("Solution part 2:", solution_2)


if __name__ == '__main__':
    main()
