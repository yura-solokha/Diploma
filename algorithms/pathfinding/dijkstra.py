import heapq
from typing import Callable, List, Tuple
from .base import PathfindingAlgorithm, Coord, Grid
from app.utils.path_utils import reconstruct_path_simple

class Dijkstra(PathfindingAlgorithm):
    def search(
        self,
        start: Coord,
        end:   Coord,
        grid:  Grid,
        get_neighbors: Callable[[Coord], List[Coord]],
        visit_callback: Callable[[Coord], None] = None
    ) -> List[Coord]:
        dist = {start: 0}
        came_from = {}
        visited = set()
        heap = [(0, start)]

        while heap:
            d, current = heapq.heappop(heap)
            if current in visited:
                continue
            visited.add(current)
            if visit_callback:
                visit_callback(current)
            if current == end:
                return reconstruct_path_simple(came_from, current)

            for nbr in get_neighbors(current):
                nd = d + 1
                if nd < dist.get(nbr, float('inf')):
                    dist[nbr] = nd
                    came_from[nbr] = current
                    heapq.heappush(heap, (nd, nbr))

        return []