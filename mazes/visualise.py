import math

import cairo

from mazes import Maze, Coord


def draw_maze(
    filename: str,
    maze: Maze,
    start: Coord,
    end: Coord,
    scale: int = 10,
    margin: int = 10,
    line_width: float = 0.1,
):
    image_size = (maze.size * scale) + (2 * margin)
    surface = cairo.SVGSurface(filename, image_size, image_size)
    ctx = cairo.Context(surface)

    # prepare for drawing
    ctx.translate(margin, margin)
    ctx.scale(scale, scale)
    ctx.set_source_rgb(0.0, 0.0, 0.0)
    ctx.set_line_width(line_width)
    ctx.set_line_cap(cairo.LINE_CAP_SQUARE)

    # checkerboard iteration pattern
    for y in range(maze.size):
        for x in range(0, maze.size, 2):
            x = x + (y % 2)
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
    ctx.move_to(0, 0)
    ctx.line_to(maze.size, 0)
    ctx.line_to(maze.size, maze.size)
    ctx.line_to(0, maze.size)
    ctx.line_to(0, 0)
    ctx.stroke()

    # draw start and end points
    ctx.set_source_rgb(1.0, 0.0, 0.0)
    ctx.arc(start[0] + 0.5, start[1] + 0.5, 0.4, 0.0, math.pi * 2)
    ctx.stroke()

    ctx.set_source_rgb(0.0, 0.0, 1.0)
    ctx.arc(end[0] + 0.5, end[1] + 0.5, 0.4, 0.0, math.pi * 2)
    ctx.stroke()

    surface.finish()
