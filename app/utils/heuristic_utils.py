from typing import Tuple
import math

Coord = Tuple[int, int]

def manhattan(a: Coord, b: Coord) -> float:
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def euclidean(a: Coord, b: Coord) -> float:
    return math.hypot(a[0] - b[0], a[1] - b[1])

def chebyshev(a: Coord, b: Coord) -> float:
    return max(abs(a[0] - b[0]), abs(a[1] - b[1]))

def octile(a: Coord, b: Coord) -> float:
    dx = abs(a[0] - b[0])
    dy = abs(a[1] - b[1])
    f = math.sqrt(2) - 1
    return f * min(dx, dy) + max(dx, dy)

# Універсальна функція вибору евристики
def calculate_heuristic(a: Coord, b: Coord, method: str = "manhattan") -> float:
    """
    method: один із "manhattan", "euclidean", "chebyshev", "octile"
    """
    if method == "euclidean":
        return euclidean(a, b)
    if method == "chebyshev":
        return chebyshev(a, b)
    if method == "octile":
        return octile(a, b)
    # за замовчуванням манхеттен
    return manhattan(a, b)