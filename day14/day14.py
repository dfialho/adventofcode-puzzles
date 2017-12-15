from typing import Iterator, Dict, Tuple, NewType, Set

import hashing

Position = NewType('Position', Tuple[int, int])


def hashes(key: str, n: int) -> Iterator[str]:
    """ Generates the *n* hash strings for the given *key* """
    for i in range(n):
        yield hashing.knot_hash(f"{key}-{i}")


def bits(hash_str: str) -> Iterator[str]:
    """ Generates each bit in the given hash string *hash_str* """
    for character in hash_str:
        for bit in f"{int(character, 16):04b}":
            yield bit


def iter_used_squares(key: str) -> Iterator[Position]:
    """ Iterates over all used squares in the grid generated from the given *key* """
    for y, hash_str in enumerate(hashes(key, n=128)):
        for x, bit in enumerate(bits(hash_str)):
            if bit == '1':
                yield (x, y)


class Graph:

    def __init__(self):
        self._nodes: Dict[Position, Set[Position]] = {}

    def add_edge(self, node1: Position, node2: Position):
        if node1 in self._nodes:
            self._nodes[node1].add(node2)
            self._nodes[node2].add(node1)

    def add_node(self, node: Position):
        self._nodes[node] = set()

    def neighbors(self, node: Position):
        return self._nodes[node]

    def nodes(self) -> Iterator[Position]:
        return iter(self._nodes.keys())

    def __str__(self):
        return str(self._nodes)


def build_graph(nodes: Iterator[Position]) -> Graph:
    """ Builds a graph connecting all used squares """
    graph = Graph()

    for x, y in nodes:
        node = (x, y)
        graph.add_node(node)

        # Link with top node
        graph.add_edge((x, y - 1), node)
        # Link with left_node
        graph.add_edge((x - 1, y), node)

    return graph


def count_groups(graph: Graph):
    """ Runs a DFSs to find all strongly-connected components (the groups) """
    visited: Set[Position] = set()
    non_visited = set(graph.nodes())
    count = 0

    while len(non_visited) > 0:
        start_node = non_visited.pop()
        visited.add(start_node)
        stack = [start_node]
        count += 1

        while len(stack) > 0:
            node = stack.pop()

            for neighbor in graph.neighbors(node):
                if neighbor not in visited:
                    stack.append(neighbor)
                    visited.add(neighbor)
                    non_visited.remove(neighbor)

    return count


def count_used(key: str) -> int:
    return sum(1 for hash_str in hashes(key, n=128) for bit in bits(hash_str) if bit == '1')


def input(path: str) -> str:
    with open(path) as file:
        return file.read()


def main():
    #
    # Part 1
    #
    print("Solution part 1:", count_used(input("input.txt")))

    #
    # Part 2
    #
    print("Solution part 2:", count_groups(build_graph(iter_used_squares(input("input.txt")))))


if __name__ == '__main__':
    main()
