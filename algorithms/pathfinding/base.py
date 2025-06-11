from abc import ABC, abstractmethod
from typing import Callable, List, Tuple

Coord = Tuple[int, int]
Grid  = List[List[int]]

class PathfindingAlgorithm(ABC):
    @abstractmethod
    def search(
        self,
        start: Coord,
        end: Coord,
        grid: Grid,
        get_neighbors: Callable[[Coord], List[Coord]],
        visit_callback: Callable[[Coord], None] = None
    ) -> List[Coord]:
        """
        Виконує пошук шляху від start до end.
        Повертає список координат шляху (включно зі start та end) або пустий список.
        visit_callback викликається для кожної відвіданої вершини.
        """
        pass