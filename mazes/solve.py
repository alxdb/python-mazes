from mazes import Maze, Coord


def basic_solve(maze: Maze, start: Coord, end: Coord) -> list[Coord]:
    def taxicab_distance(coord: Coord) -> int:
        return abs(coord[0] - end[0]) + abs(coord[1] - end[1])

    path = [start]
    seen = set(start)
    while True:
        try:
            current = path[-1]
        except IndexError:
            raise ValueError(f"no solution for {start} to {end}")

        unseen = [n for n in maze.paths[current] if n not in seen]
        if unseen:
            step = min(unseen, key=taxicab_distance)
            path.append(step)
            if step == end:
                break
            seen.add(step)
        else:
            path.pop()

    return path
