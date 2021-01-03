import math

import cairo

import mazes


def draw_maze(maze: mazes.Maze, start: mazes.Coord, end: mazes.Coord,
              scale=10, line_width=0.1):
    cell_size = scale
    margin = 10
    image_size = (maze.size * cell_size) + (2 * margin)
    surface = cairo.SVGSurface("image.svg", image_size, image_size)
    ctx = cairo.Context(surface)

    ctx.translate(margin, margin)
    ctx.scale(cell_size, cell_size)
    ctx.set_source_rgb(0.0, 0.0, 0.0)
    ctx.set_line_width(line_width)
    ctx.set_line_cap(cairo.LINE_CAP_SQUARE)

    # checkerboard pattern
    for y in range(maze.size):
        for x in range(0, maze.size, 2):
            x = x + (y % 2)
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

    ctx.move_to(0, 0)
    ctx.line_to(maze.size, 0)
    ctx.line_to(maze.size, maze.size)
    ctx.line_to(0, maze.size)
    ctx.line_to(0, 0)
    ctx.stroke()

    ctx.set_source_rgb(1.0, 0.0, 0.0)
    ctx.arc(start[0] + 0.5, start[1] + 0.5, 0.4, 0.0, math.pi * 2)
    ctx.stroke()

    ctx.set_source_rgb(0.0, 0.0, 1.0)
    ctx.arc(end[0] + 0.5, end[1] + 0.5, 0.4, 0.0, math.pi * 2)
    ctx.stroke()

    surface.finish()
