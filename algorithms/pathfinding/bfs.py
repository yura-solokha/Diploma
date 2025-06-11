from collections import deque
from typing import Callable, List, Tuple
from .base import PathfindingAlgorithm, Coord, Grid
from app.utils.path_utils import reconstruct_path_simple

class BFS(PathfindingAlgorithm):
    def search(
        self,
        start: Coord,
        end:   Coord,
        grid:  Grid,
        get_neighbors: Callable[[Coord], List[Coord]],
        visit_callback: Callable[[Coord], None] = None
    ) -> List[Coord]:
        queue = deque([start])
        came_from = {}
        visited = {start}

        while queue:
            current = queue.popleft()
            if visit_callback:
                visit_callback(current)
            if current == end:
                return reconstruct_path_simple(came_from, current)

            for nbr in get_neighbors(current):
                if nbr not in visited:
                    visited.add(nbr)
                    came_from[nbr] = current
                    queue.append(nbr)

        return []