from typing import Callable, List, Tuple
from .base import PathfindingAlgorithm, Coord, Grid
from app.utils.path_utils import reconstruct_path_simple

class DFS(PathfindingAlgorithm):
    def search(
        self,
        start: Coord,
        end:   Coord,
        grid:  Grid,
        get_neighbors: Callable[[Coord], List[Coord]],
        visit_callback: Callable[[Coord], None] = None
    ) -> List[Coord]:
        stack = [start]
        came_from = {}
        visited = set()

        while stack:
            current = stack.pop()
            if current in visited:
                continue
            visited.add(current)
            if visit_callback:
                visit_callback(current)
            if current == end:
                return reconstruct_path_simple(came_from, current)

            for nbr in get_neighbors(current):
                if nbr not in visited:
                    came_from[nbr] = current
                    stack.append(nbr)

        return []