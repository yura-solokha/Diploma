# app/controllers/grid_controller.py

from PyQt5.QtCore import QTimer
from typing import List, Tuple
from models.grid_model import GridModel
from controllers.algorithm_controller import AlgorithmController

Coord = Tuple[int,int]

class GridController:
    def __init__(self, model: GridModel, view):
        self.model  = model
        self.view   = view
        self.algo   = AlgorithmController()

        self.timer = QTimer()
        self.timer.timeout.connect(self._on_timer_tick)
        self._animation_queue: List[Tuple[str, Coord]] = []

        self.view.run_clicked.connect(self.on_run_clicked)
        self.view.generate_clicked.connect(self.on_generate_clicked)
        self.view.clear_grid_clicked.connect(self.on_clear_grid)
        self.view.clear_path_clicked.connect(self.on_clear_path)
        self.view.stop_animation_clicked.connect(self.on_stop_animation)
        self.view.cell_toggled.connect(self.on_cell_toggled)
        self.view.speed_changed.connect(self.on_speed_changed)

    def on_cell_toggled(self, r: int, c: int):
        self.model.toggle_obstacle(r, c)
        self.view.update_cell(r, c, self.model.cells[r][c].cell_type)

    def on_run_clicked(self):
        self.model.clear_path_and_visited()
        self.view.refresh_grid()

        start = self.model.start_coord()
        end   = self.model.end_coord()
        grid  = self.model.to_grid_array()
        heuristic = self.view.get_heuristic()

        visited, path = self.algo.run(
            name          = self.view.get_algorithm(),
            start         = start,
            end           = end,
            grid          = grid,
            get_neighbors = lambda coord: [
                (c.row, c.col) for c in self.model.get_neighbors(*coord)
            ],
            heuristic     = heuristic
        )
        self._animation_queue = [
            ("visit", coord) for coord in visited
        ] + [
            ("path", coord) for coord in path
        ]
        self.view.set_stats(
            time_ms   = 0,
            visited_n = len(visited),
            path_len  = len(path)
        )
        self._start_animation()

    def _start_animation(self):
        interval = self.view.get_speed()  # мс
        self.timer.start(interval)

    def _on_timer_tick(self):
        if not self._animation_queue:
            self.timer.stop()
            return

        typ, (r, c) = self._animation_queue.pop(0)
        cell = self.model.cells[r][c]
        if typ == "visit":
            cell.mark_visited()
        else:
            cell.mark_path()

        self.view.update_cell(r, c, cell.cell_type)

    def on_generate_clicked(self):
        self.model.reset(preserve_start_end=True)
        self.view.refresh_grid()

        method = self.view.get_maze_method()
        gen = None
        if method == "Prim":
            from algorithms.maze.prim import PrimMaze
            gen = PrimMaze().generate(self.model.rows, self.model.cols)
        elif method == "Backtrack":
            from algorithms.maze.recursive_backtrack import RecursiveBacktrackMaze
            gen = RecursiveBacktrackMaze().generate(self.model.rows, self.model.cols)
        else:
            from algorithms.maze.recursive_division import RecursiveDivisionMaze
            gen = RecursiveDivisionMaze().generate(self.model.rows, self.model.cols)

        self._animation_queue = []
        for grid_state in gen:
            for r in range(self.model.rows):
                for c in range(self.model.cols):
                    cell = self.model.cells[r][c]
                    if (r,c) in (self.model.start_coord(), self.model.end_coord()):
                        continue
                    if grid_state[r][c] == 1:
                        cell.is_obstacle = True
                    else:
                        cell.is_obstacle = False
                    self._animation_queue.append(
                        ("set", (r,c), cell.cell_type)
                    )
        self._start_animation()

    def on_clear_grid(self):
        self.timer.stop()
        self.model.reset(preserve_start_end=False)
        self.view.refresh_grid()
        self.view.set_stats("-", "-", "-")

    def on_clear_path(self):
        self.timer.stop()
        self.model.clear_path_and_visited()
        self.view.refresh_grid()
        self.view.set_stats(time_ms="-", visited_n="-", path_len="-")

    def on_stop_animation(self):
        self.timer.stop()

    def on_speed_changed(self, new_speed: int):
        if self.timer.isActive():
            self.timer.setInterval(new_speed)