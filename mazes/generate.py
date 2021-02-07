from mazes import Maze, Coord
import random


def random_walk(size: int) -> tuple[Maze, list[Coord]]:
    maze = Maze(size)

    start = (random.randrange(size), random.randrange(size))

    current_solution = [start]
    longest_solution = current_solution.copy()
    seen = {start}
    while len(seen) < (size ** 2):
        current = current_solution[-1]
        unvisited_neighbours = [
            n for n in maze.neighbours(current) if n not in seen
        ]
        if unvisited_neighbours:
            chosen = random.choice(unvisited_neighbours)
            current_solution.append(chosen)
            seen.add(chosen)
            maze.connect_path(current, chosen)
        else:
            if len(current_solution) > len(longest_solution):
                longest_solution = current_solution.copy()
            current_solution.pop()

    return maze, longest_solution
