from typing import Dict, Tuple, List

Coord = Tuple[int, int]
CameFrom = Dict[Coord, Coord]

def reconstruct_path(came_from: CameFrom, current: Coord) -> List[Coord]:
    path = [current]
    while current in came_from:
        current = came_from[current]
        path.append(current)
    path.reverse()
    return path

def reconstruct_path_simple(came_from: CameFrom, current: Coord) -> List[Coord]:
    path = [current]
    while current in came_from:
        current = came_from[current]
        path.append(current)
    path.reverse()
    return path