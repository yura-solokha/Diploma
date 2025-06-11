from typing import Literal

CellType = Literal["default", "start", "end", "obstacle", "visited", "path"]

class CellModel:
    def __init__(self, row: int, col: int):
        self.row: int = row
        self.col: int = col
        self.reset()

    def reset(self) -> None:
        self.is_obstacle: bool = False
        self.is_start:    bool = False
        self.is_end:      bool = False
        self.is_visited:  bool = False
        self.is_path:     bool = False

    def set_start(self) -> None:
        self.reset()
        self.is_start = True

    def set_end(self) -> None:
        self.reset()
        self.is_end = True

    def toggle_obstacle(self) -> None:
        if self.is_start or self.is_end:
            return
        self.is_obstacle = not self.is_obstacle

    def mark_visited(self) -> None:
        if not (self.is_start or self.is_end or self.is_obstacle):
            self.is_visited = True

    def mark_path(self) -> None:
        if not (self.is_start or self.is_end or self.is_obstacle):
            self.is_path = True

    @property
    def cell_type(self) -> CellType:
        if self.is_start:
            return "start"
        if self.is_end:
            return "end"
        if self.is_obstacle:
            return "obstacle"
        if self.is_path:
            return "path"
        if self.is_visited:
            return "visited"
        return "default"