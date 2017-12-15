from typing import List, Iterator, Dict, Tuple, NewType, Set

import hashing


def hashes(key: str, n: int) -> Iterator[str]:
    """ Generates the *n* hash strings for the given *key* """
    for i in range(n):
        yield hashing.knot_hash(f"{key}-{i}")


def to_bits(hash_str: str) -> str:
    """ Converts hexadecimal *hash_str* to a string of bits """
    return "".join(f"{int(character, 16):04b}" for character in hash_str)


Position = NewType('Position', Tuple[int, int])


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


def count_groups(graph: Graph):
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


def nodes_iter(key: str) -> Iterator[Tuple[Position]]:
    for y, hash_str in enumerate(hashes(key, n=128)):
        for x, bit in enumerate(to_bits(hash_str)):
            if bit == '1':
                yield (x, y)


def build_graph(nodes: Iterator[Tuple[Position]]) -> Graph:
    graph = Graph()

    for x, y in nodes:
        node = (x, y)
        graph.add_node(node)

        if y > 0:
            top_node = (x, y - 1)
            graph.add_edge(top_node, node)

        if x > 0:
            left_node = (x - 1, y)
            graph.add_edge(left_node, node)

    return graph


def build_grid(key: str) -> List[str]:
    return [to_bits(hash_str) for hash_str in hashes(key, n=128)]


def count_used(grid: List[str]) -> int:
    return sum(row.count('1') for row in grid)


def input(path: str) -> str:
    with open(path) as file:
        return file.read()


def main():
    #
    # Part 1
    #
    print("Solution part 1:", count_used(build_grid(input("input.txt"))))

    #
    # Part 2
    #
    print("Solution part 2:", count_groups(build_graph(nodes_iter(input("input.txt")))))


if __name__ == '__main__':
    main()
