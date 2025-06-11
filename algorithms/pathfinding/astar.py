import heapq
from typing import Callable, List, Tuple
from .base import PathfindingAlgorithm, Coord, Grid
from app.utils.path_utils      import reconstruct_path
from app.utils.heuristic_utils import calculate_heuristic

class AStar(PathfindingAlgorithm):
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
        rows, cols = len(grid), len(grid[0])
        dirs = [(0,1),(1,0),(-1,0),(0,-1)]
        if self.diagonal:
            dirs += [(1,1),(1,-1),(-1,1),(-1,-1)]

        open_heap = []
        heapq.heappush(open_heap, (0, start))
        g_cost = {start: 0}
        came_from = {}

        while open_heap:
            f, current = heapq.heappop(open_heap)
            if visit_callback:
                visit_callback(current)
            if current == end:
                return reconstruct_path(came_from, current)

            for dr, dc in dirs:
                nr, nc = current[0] + dr, current[1] + dc
                nxt = (nr, nc)
                if not (0 <= nr < rows and 0 <= nc < cols):
                    continue
                if grid[nr][nc] == 1:  # стіна
                    continue

                tentative = g_cost[current] + 1
                if tentative < g_cost.get(nxt, float('inf')):
                    g_cost[nxt] = tentative
                    came_from[nxt] = current
                    h = calculate_heuristic(nxt, end, self.heuristic)
                    heapq.heappush(open_heap, (tentative + h, nxt))

        return []