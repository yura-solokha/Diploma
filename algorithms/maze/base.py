from abc import ABC, abstractmethod
from typing import Generator, List, Tuple

Coord = Tuple[int,int]
Grid  = List[List[int]]

class MazeGenerator(ABC):
    @abstractmethod
    def generate(self, rows: int, cols: int) -> Generator[Grid, None, None]:
        """
        Генерує лабіринт як послідовність станів сітки:
        кожен yield — новий стан Grid (0 — прохід, 1 — стіна).
        """
        pass