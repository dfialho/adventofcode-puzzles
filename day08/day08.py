from typing import Dict, Iterator, List

import operator
from abc import ABC, abstractmethod
from collections import defaultdict

#
# Structure used to represent the registers and hold their values
#
registers: Dict[str, int] = defaultdict(int)
highest_register_value = 0


class Expression(ABC):

    @abstractmethod
    def eval(self):
        pass


class Operation(ABC):

    @abstractmethod
    def eval(self):
        pass


class Increment(Operation):

    def __init__(self, register: str, value: int):
        self.value = value
        self.register = register

    def eval(self):
        global highest_register_value

        registers[self.register] += self.value
        highest_register_value = max(registers[self.register], highest_register_value)


class Decrement(Operation):

    def __init__(self, register: str, value: int):
        self.value = value
        self.register = register

    def eval(self):
        global highest_register_value

        registers[self.register] -= self.value
        highest_register_value = max(registers[self.register], highest_register_value)


class Condition(ABC):

    @abstractmethod
    def is_true(self) -> bool:
        pass


class EqualTo(Condition):

    def __init__(self, register: str, value: int):
        self.register = register
        self.value = value

    def is_true(self) -> bool:
        return registers[self.register] == self.value


class DifferentFrom(Condition):

    def __init__(self, register: str, value: int):
        self.register = register
        self.value = value

    def is_true(self) -> bool:
        return registers[self.register] != self.value


class LowerThan(Condition):

    def __init__(self, register: str, value: int):
        self.register = register
        self.value = value

    def is_true(self) -> bool:
        return registers[self.register] < self.value


class LowerThanOrEqualTo(Condition):

    def __init__(self, register: str, value: int):
        self.register = register
        self.value = value

    def is_true(self) -> bool:
        return registers[self.register] <= self.value


class HigherThan(Condition):

    def __init__(self, register: str, value: int):
        self.register = register
        self.value = value

    def is_true(self) -> bool:
        return registers[self.register] > self.value


class HigherThanOrEqualTo(Condition):

    def __init__(self, register: str, value: int):
        self.register = register
        self.value = value

    def is_true(self) -> bool:
        return registers[self.register] >= self.value


class IfStatement(Expression):

    def __init__(self, operation: Operation, condition: Condition):
        self.operation = operation
        self.condition = condition

    def eval(self):
        if self.condition.is_true():
            self.operation.eval()


class Program:

    def __init__(self):
        self.expressions: List[Expression] = []

    def run(self):
        for expression in self.expressions:
            expression.eval()

    def add_expression(self, expression: Expression):
        self.expressions.append(expression)


class Parser:
    operations = {
        'inc': Increment,
        'dec': Decrement,
    }

    conditions = {
        '==': EqualTo,
        '!=': DifferentFrom,
        '<': LowerThan,
        '>': HigherThan,
        '<=': LowerThanOrEqualTo,
        '>=': HigherThanOrEqualTo,
    }

    def parse(self, path: str) -> Program:
        program = Program()
        for line in lines(path):
            self.parse_line(program, line)

        return program

    def parse_line(self, program: Program, line: str):
        op_register, op_label, op_value, _, cond_register, cond_label, cond_value = line.split(" ")

        operation = self.operations[op_label]
        condition = self.conditions[cond_label]

        program.add_expression(IfStatement(
            operation=operation(op_register, int(op_value)),
            condition=condition(cond_register, int(cond_value))
        ))


def lines(path: str) -> Iterator[str]:
    with open(path) as file:
        for line in file:
            yield line


def main():
    parser = Parser()
    program = parser.parse("input.txt")
    program.run()

    print("Solution part 1:", max(registers.items(), key=operator.itemgetter(1)))
    print("Solution part 2:", highest_register_value)


if __name__ == '__main__':
    main()
