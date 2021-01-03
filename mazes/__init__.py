from typing import Set, Dict, Tuple, Iterator

Coord = Tuple[int, int]


class Maze:
    def __init__(self, size: int):
        assert size > 1
        self.size: int = size
        self.paths: Dict[Coord, Set[Coord]] = {}

    def neighbours(self, coord: Coord) -> Iterator[Coord]:
        for x, y in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            n_x = coord[0] + x
            n_y = coord[1] + y
            if 0 <= n_x < self.size and 0 <= n_y < self.size:
                yield coord[0] + x, coord[1] + y

    def connect_path(self, a: Coord, b: Coord) -> None:
        self.paths.setdefault(a, set()).add(b)
        self.paths.setdefault(b, set()).add(a)
