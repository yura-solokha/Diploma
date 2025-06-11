from typing import List, Tuple, Callable
from algorithms.pathfinding.astar       import AStar
from algorithms.pathfinding.bfs         import BFS
from algorithms.pathfinding.dfs         import DFS
from algorithms.pathfinding.dijkstra    import Dijkstra
from algorithms.pathfinding.greedy      import GreedyBestFirst

Coord = Tuple[int,int]
Grid  = List[List[int]]

class AlgorithmController:
    def __init__(self):
        pass

    def run(
        self,
        name: str,
        start: Coord,
        end:   Coord,
        grid:  Grid,
        get_neighbors: Callable[[Coord], List[Coord]],
        heuristic: str = "manhattan"
    ) -> Tuple[List[Coord], List[Coord]]:
        if name == "A*":
            algo = AStar(diagonal=False, heuristic=heuristic)
        elif name == "Dijkstra":
            algo = Dijkstra()
        elif name == "BFS":
            algo = BFS()
        elif name == "DFS":
            algo = DFS()
        elif name == "Greedy":
            algo = GreedyBestFirst(diagonal=False, heuristic=heuristic)
        else:
            raise ValueError(f"Невідомий алгоритм: {name}")

        visited_order: List[Coord] = []
        path = algo.search(
            start, end, grid, get_neighbors,
            visit_callback=lambda coord: visited_order.append(coord)
        )
        return visited_order, path