from typing import List, Tuple

from mazes import Maze, Coord
import random


def random_walk(size: int) -> Tuple[Maze, List[Coord]]:
    maze = Maze(size)

    start = (random.randrange(size), random.randrange(size))

    current = start
    current_solution = []
    longest_solution = []
    while len(maze.paths) < (size * size):
        unvisited_neighbours = [
            neighbour
            for neighbour in maze.neighbours(current)
            if neighbour not in maze.paths
        ]
        if len(unvisited_neighbours) > 0:
            current_solution.append(current)
            chosen = random.choice(unvisited_neighbours)
            maze.connect_path(current, chosen)
            current = chosen
            if len(current_solution) > len(longest_solution):
                longest_solution = current_solution.copy()
                longest_solution.append(current)
        else:
            current = current_solution.pop()

    return maze, longest_solution
