from typing import List, Optional, Tuple
from .cell_model import CellModel

Coord = Tuple[int, int]

class GridModel:
    def __init__(self, rows: int, cols: int):
        self.rows: int = rows
        self.cols: int = cols
        self.cells: List[List[CellModel]] = [
            [CellModel(r, c) for c in range(cols)]
            for r in range(rows)
        ]
        self.start: Optional[CellModel] = None
        self.end:   Optional[CellModel] = None

    def reset(self, preserve_start_end: bool = False) -> None:
        for row in self.cells:
            for cell in row:
                cell.reset()
        if preserve_start_end:
            if self.start:
                self.start.set_start()
            if self.end:
                self.end.set_end()
        else:
            self.start = None
            self.end = None

    def set_start(self, r: int, c: int) -> None:
        if self.start:
            self.start.reset()
        cell = self.cells[r][c]
        cell.set_start()
        self.start = cell

    def set_end(self, r: int, c: int) -> None:
        if self.end:
            self.end.reset()
        cell = self.cells[r][c]
        cell.set_end()
        self.end = cell

    def toggle_obstacle(self, r: int, c: int) -> None:
        cell = self.cells[r][c]
        cell.toggle_obstacle()

    def get_neighbors(self, r: int, c: int) -> List[CellModel]:
        neighbors: List[CellModel] = []
        for dr, dc in [(0,1),(1,0),(0,-1),(-1,0)]:
            rr, cc = r + dr, c + dc
            if 0 <= rr < self.rows and 0 <= cc < self.cols:
                neigh = self.cells[rr][cc]
                if not neigh.is_obstacle:
                    neighbors.append(neigh)
        return neighbors

    def clear_path_and_visited(self) -> None:
        for row in self.cells:
            for cell in row:
                cell.is_visited = False
                cell.is_path = False

    def to_grid_array(self) -> List[List[int]]:
        return [
            [1 if cell.is_obstacle else 0 for cell in row]
            for row in self.cells
        ]

    def start_coord(self) -> Coord:
        assert self.start, "Start not set"
        return (self.start.row, self.start.col)

    def end_coord(self) -> Coord:
        assert self.end, "End not set"
        return (self.end.row, self.end.col)