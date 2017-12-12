from typing import Dict, Set

from collections import defaultdict


class Graph:

    def __init__(self):
        self._nodes: Dict[int, Set[int]] = defaultdict(set)

    def add_edge(self, node1: int, node2: int):
        self._nodes[node1].add(node2)
        self._nodes[node2].add(node1)

    def neighbors(self, node: int):
        return self._nodes[node]

    def __str__(self):
        return str(self._nodes)


def count_group_nodes(graph: Graph, start_node: int):
    stack = [start_node]
    visited: Set[int] = {start_node}
    count = 0

    while len(stack) > 0:
        node = stack.pop()
        count += 1

        for neighbor in graph.neighbors(node):
            if neighbor not in visited:
                stack.append(neighbor)
                visited.add(neighbor)

    return count


def read_graph(path: str) -> Graph:
    with open(path) as file:
        graph = Graph()
        for line in file:
            node, neighbors = line.split(" <-> ")

            for neighbor in map(int, neighbors.split(", ")):
                graph.add_edge(int(node), neighbor)

    return graph


def main():
    #
    # Part 1
    #

    print("Solution part 1:", count_group_nodes(read_graph("input.txt"), start_node=0))

    #
    # Part 2
    #


if __name__ == '__main__':
    main()
