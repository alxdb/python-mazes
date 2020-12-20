from typing import Tuple, List, Iterator, Optional
import random


class Maze:
    class Room:
        def __init__(self, x: int, y: int, size: int):
            self._x: int = x
            self._y: int = y

            # doors are stored in natural order: N, E, S, W
            self._doors: List[Optional[bool]] = [False, ] * 4

            # set edge doors to None
            if x == 0:
                self._doors[3] = None
            elif x % (size - 1) == 0:
                self._doors[1] = None
            if y == 0:
                self._doors[0] = None
            elif y % (size - 1) == 0:
                self._doors[2] = None

        @property
        def coords(self) -> Tuple[int, int]:
            return self._x, self._y

        @property
        def doors(self) -> List[Optional[bool]]:
            return self._doors

        def open_doors(self) -> List[int]:
            return [i for i, door in enumerate(self._doors) if door]

        def closed_doors(self) -> List[int]:
            return [i for i, door in enumerate(self._doors) if door is False]

        def change_door(self, direction: int, state: bool) -> None:
            try:
                if self._doors[direction] is not None:
                    self._doors[direction] = state
            except IndexError:
                raise ValueError(f"invalid direction ({direction})")

        def open_door(self, direction: int) -> None:
            self.change_door(direction, True)

        def close_door(self, direction: int) -> None:
            self.change_door(direction, False)

        def neighbour_coords(self, direction: int) -> Tuple[int, int]:
            try:
                if self._doors[direction] is None:
                    raise RuntimeError(f"no neighbour in that direction")
            except IndexError:
                raise ValueError(f"invalid direction ({direction})")

            if direction == 0:
                return self.coords[0], self.coords[1] - 1
            if direction == 1:
                return self.coords[0] + 1, self.coords[1]
            if direction == 2:
                return self.coords[0], self.coords[1] + 1
            if direction == 3:
                return self.coords[0] - 1, self.coords[1]

    def __init__(self, size: int):
        if size < 2:
            raise ValueError(f"Size ({size}) must be greater than 2")
        self._rooms: List[List[Maze.Room]] = [
            [self.Room(x, y, size) for x in range(size)] for y in range(size)
        ]

        # pick a random room on the edge of the maze to start on
        coord = (random.randint(0, 1) * (size - 1), random.randrange(0, size))
        if random.randint(0, 1):
            coord = (coord[1], coord[0])
        current_room = self[coord]

        visited_rooms = set()
        solution = []
        while len(visited_rooms) < (size * size):
            visited_rooms.add(current_room)
            closed_doors = current_room.closed_doors()
            if len(closed_doors) > 0:
                solution.append(current_room.coords)
                direction = random.choice(closed_doors)
                current_room.open_door(direction)
                current_room = self[current_room.neighbour_coords(direction)]
                current_room.open_door((direction + 2) % 4)
            else:
                current_room = self[solution.pop()]

    def __iter__(self) -> Iterator[Room]:
        return (room for row in self._rooms for room in row)

    def __getitem__(self, coords: Tuple[int, int]) -> Room:
        try:
            return self._rooms[coords[1]][coords[0]]
        except IndexError:
            raise IndexError(f"coordinates out of range: {coords}")
