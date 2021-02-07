import math

import cairo

from mazes import Maze, Coord


BACKGROUND = cairo.SolidPattern(0.15, 0.15, 0.15)
FOREGROUND = cairo.SolidPattern(0.8, 0.8, 0.8)

START = cairo.SolidPattern(0.8, 0.2, 0.2)
END = cairo.SolidPattern(0.2, 0.8, 0.2)
PATH = cairo.SolidPattern(0.2, 0.2, 0.8)


def draw_maze(
    filename: str,
    maze: Maze,
    solution: list[Coord],
    scale: int = 10,
    margin: int = 10,
    line_width: float = 0.1,
) -> None:
    start = solution[0]
    end = solution[-1]

    image_size = (maze.size * scale) + (2 * margin)
    surface = cairo.SVGSurface(filename, image_size, image_size)
    ctx = cairo.Context(surface)

    # background
    ctx.set_source(BACKGROUND)
    ctx.rectangle(0, 0, image_size, image_size)
    ctx.fill()

    # prepare for drawing
    ctx.translate(margin, margin)
    ctx.scale(scale, scale)

    # checkerboard iteration pattern
    ctx.set_source(FOREGROUND)
    ctx.set_line_width(line_width)
    ctx.set_line_cap(cairo.LINE_CAP_SQUARE)
    for y in range(maze.size):
        for x in range(0, maze.size, 2):
            x = x + (y % 2)
            if x >= maze.size:
                continue
            # map neighbours to edge lines
            for neighbour in maze.neighbours((x, y)):
                if neighbour not in maze.paths[(x, y)]:
                    if neighbour == (x, y - 1):
                        ctx.move_to(x, y)
                        ctx.line_to(x + 1, y)
                    elif neighbour == (x + 1, y):
                        ctx.move_to(x + 1, y)
                        ctx.line_to(x + 1, y + 1)
                    elif neighbour == (x, y + 1):
                        ctx.move_to(x, y + 1)
                        ctx.line_to(x + 1, y + 1)
                    elif neighbour == (x - 1, y):
                        ctx.move_to(x, y)
                        ctx.line_to(x, y + 1)
                ctx.stroke()

    # draw borders
    ctx.move_to(start[0] + 0.5, start[1] + 0.5)
    ctx.move_to(0, 0)
    ctx.line_to(maze.size, 0)
    ctx.line_to(maze.size, maze.size)
    ctx.line_to(0, maze.size)
    ctx.line_to(0, 0)
    ctx.stroke()

    # solution
    ctx.set_source(PATH)
    ctx.move_to(start[0] + 0.5, start[1] + 0.5)
    for step in solution[1:]:
        ctx.line_to(step[0] + 0.5, step[1] + 0.5)
    ctx.stroke()

    # draw start and end points
    ctx.set_source(START)
    ctx.arc(start[0] + 0.5, start[1] + 0.5, 0.4, 0.0, math.pi * 2)
    ctx.fill()

    ctx.set_source(END)
    ctx.arc(end[0] + 0.5, end[1] + 0.5, 0.4, 0.0, math.pi * 2)
    ctx.fill()

    surface.finish()
