import random
from typing import Generator, List, Tuple
from .base import MazeGenerator, Coord, Grid

class PrimMaze(MazeGenerator):
    def generate(self, rows: int, cols: int) -> Generator[Grid, None, None]:
        grid = [[1]*cols for _ in range(rows)]
        sr, sc = random.randrange(0, rows, 2), random.randrange(0, cols, 2)
        grid[sr][sc] = 0
        walls: List[Tuple[int,int,int,int]] = []

        def add_walls(r: int, c: int):
            for dr, dc in [(-2,0),(2,0),(0,-2),(0,2)]:
                nr, nc = r+dr, c+dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                    walls.append((r+dr//2, c+dc//2, nr, nc))

        add_walls(sr, sc)
        yield [row[:] for row in grid]

        while walls:
            wr, wc, cr, cc = walls.pop(random.randrange(len(walls)))
            if grid[cr][cc] == 1:
                grid[wr][wc] = 0
                grid[cr][cc] = 0
                add_walls(cr, cc)
                yield [row[:] for row in grid]