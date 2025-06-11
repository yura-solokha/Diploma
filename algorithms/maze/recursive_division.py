import random
from typing import Generator, List
from .base import MazeGenerator, Grid

class RecursiveDivisionMaze(MazeGenerator):
    def generate(self, rows: int, cols: int) -> Generator[Grid, None, None]:
        grid = [[1]*cols for _ in range(rows)]
        for y in range(1, rows-1):
            for x in range(1, cols-1):
                grid[y][x] = 0
        yield [row[:] for row in grid]

        def choose_orient(w: int, h: int) -> str:
            if w < h: return 'H'
            if h < w: return 'V'
            return random.choice(['H','V'])

        def divide(x: int, y: int, w: int, h: int, orient: str):
            if w < 3 or h < 3:
                return
            horizontal = (orient == 'H')
            if horizontal:
                ys = [yy for yy in range(y+1, y+h-1) if yy%2==0]
                wy = random.choice(ys)
                px = random.choice([xx for xx in range(x, x+w) if xx%2==1])
                for xx in range(x, x+w):
                    grid[wy][xx] = 0 if xx==px else 1
                yield [row[:] for row in grid]
                yield from divide(x, y, w, wy-y, choose_orient(w, wy-y))
                yield from divide(x, wy+1, w, y+h-(wy+1), choose_orient(w, y+h-(wy+1)))
            else:
                xs = [xx for xx in range(x+1, x+w-1) if xx%2==0]
                wx = random.choice(xs)
                py = random.choice([yy for yy in range(y, y+h) if yy%2==1])
                for yy in range(y, y+h):
                    grid[yy][wx] = 0 if yy==py else 1
                yield [row[:] for row in grid]
                yield from divide(x, y, wx-x, h, choose_orient(wx-x, h))
                yield from divide(wx+1, y, x+w-(wx+1), h, choose_orient(x+w-(wx+1), h))

        yield from divide(1, 1, cols-2, rows-2, choose_orient(cols-2, rows-2))