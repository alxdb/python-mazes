from typing import List, Tuple

import mazes
import random


def random_walk(size: int) -> Tuple[mazes.Maze, List[mazes.Coord]]:
    maze = mazes.Maze(size)

    start = (random.randint(0, 1) * (size - 1), random.randrange(0, size))
    if random.choice([True, False]):
        start = (start[1], start[0])

    # random walk
    current = start
    solution = []
    while len(maze.paths) < (size * size):
        unvisited_neighbours = [
            neighbour for neighbour in maze.neighbours(current)
            if neighbour not in maze.paths
        ]
        if len(unvisited_neighbours) > 0:
            solution.append(current)
            chosen = random.choice(unvisited_neighbours)
            maze.connect_path(current, chosen)
            current = chosen
        else:
            current = solution.pop()

    return maze, solution
