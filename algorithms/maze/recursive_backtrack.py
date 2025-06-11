import random
from typing import Generator, List, Tuple
from .base import MazeGenerator, Coord, Grid

class RecursiveBacktrackMaze(MazeGenerator):
    def generate(self, rows: int, cols: int) -> Generator[Grid, None, None]:
        grid = [[1]*cols for _ in range(rows)]
        stack = []
        sr, sc = random.randrange(0, rows, 2), random.randrange(0, cols, 2)
        grid[sr][sc] = 0
        stack.append((sr, sc))
        yield [row[:] for row in grid]

        def neighbors(r: int, c: int):
            dirs = [(0,2),(0,-2),(2,0),(-2,0)]
            random.shuffle(dirs)
            for dr, dc in dirs:
                nr, nc = r+dr, c+dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                    yield nr, nc, r+dr//2, c+dc//2

        while stack:
            r, c = stack[-1]
            for nr, nc, wr, wc in neighbors(r, c):
                grid[wr][wc] = 0
                grid[nr][nc] = 0
                stack.append((nr, nc))
                yield [row[:] for row in grid]
                break
            else:
                stack.pop()