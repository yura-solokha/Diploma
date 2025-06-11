import heapq
from typing import Callable, List, Tuple
from .base import PathfindingAlgorithm, Coord, Grid
from app.utils.path_utils import reconstruct_path_simple
from app.utils.heuristic_utils import calculate_heuristic

class GreedyBestFirst(PathfindingAlgorithm):
    def __init__(self, diagonal: bool = False, heuristic: str = "manhattan"):
        self.diagonal = diagonal
        self.heuristic = heuristic

    def search(
        self,
        start: Coord,
        end:   Coord,
        grid:  Grid,
        get_neighbors: Callable[[Coord], List[Coord]],
        visit_callback: Callable[[Coord], None] = None
    ) -> List[Coord]:
        open_heap = []
        heapq.heappush(open_heap, (0, start))
        came_from = {}
        visited = set()

        while open_heap:
            _, current = heapq.heappop(open_heap)
            if current in visited:
                continue
            visited.add(current)
            if visit_callback:
                visit_callback(current)
            if current == end:
                return reconstruct_path_simple(came_from, current)

            for nbr in get_neighbors(current):
                if nbr in visited:
                    continue
                came_from[nbr] = current
                h = calculate_heuristic(nbr, end, self.heuristic)
                heapq.heappush(open_heap, (h, nbr))

        return []