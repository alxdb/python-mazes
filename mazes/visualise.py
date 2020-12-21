from typing import List
import itertools

import mazes


def to_grid(maze: mazes.Maze) -> List[List[bool]]:
    grid_size = (maze.size * 2) + 1
    grid = [[False] * grid_size for _ in range(grid_size)]

    for gy, gx in itertools.product(range(grid_size), repeat=2):
        on_y = gy % 2 == 1
        on_x = gx % 2 == 1
        edge_y = gy == 0 or gy == (grid_size - 1)
        edge_x = gx == 0 or gx == (grid_size - 1)

        if on_x and on_y:
            grid[gy][gx] = True
        elif not (edge_y or edge_x):
            if on_x:
                x = gx // 2
                y1 = (gy - 1) // 2
                y2 = (gy + 1) // 2
                grid[gy][gx] = (y1, x) in maze.paths[(y2, x)]
            elif on_y:
                y = gy // 2
                x1 = (gx - 1) // 2
                x2 = (gx + 1) // 2
                grid[gy][gx] = (y, x1) in maze.paths[(y, x2)]

    return grid
