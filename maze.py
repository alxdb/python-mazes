from typing import Set, Dict, Tuple, List, Iterator
import random

Coord = Tuple[int, int]


class Maze:
    def __add_edge(self, a, b):
        # bidirectional

        if a in self.edges:
            self.edges[a].add(b)
        else:
            self.edges[a] = {b}

        if b in self.edges:
            self.edges[b].add(a)
        else:
            self.edges[b] = {a}

        # directional
        # if a < b:
        #     a, b = b, a
        #
        # if a in self.edges:
        #     self.edges[a].add(b)
        # else:
        #     self.edges[a] = {b}

    def __init__(self, size: int):
        if size < 2:
            raise ValueError("size must be > 2")

        self.edges: Dict[Coord, Set[Coord]] = {}
        self.solution: List[Coord] = []

        def neighbours(coord: Coord) -> Iterator[Coord]:
            for x, y in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                x_bound = 0 <= coord[0] + x < size
                y_bound = 0 <= coord[1] + y < size
                if x_bound and y_bound:
                    yield coord[0] + x, coord[1] + y

        # random edge node
        start = (random.randint(0, 1) * (size - 1), random.randrange(0, size))
        if random.choice([True, False]):
            start = (start[1], start[0])

        # random walk
        current = start
        while len(self.edges) < (size * size):
            unvisited_neighbours = [
                neighbour for neighbour in neighbours(current)
                if neighbour not in self.edges
            ]
            if len(unvisited_neighbours) > 0:
                self.solution.append(current)
                chosen = random.choice(unvisited_neighbours)
                self.__add_edge(current, chosen)
                current = chosen
            else:
                current = self.solution.pop()
