from PyQt5.QtWidgets import QWidget, QGridLayout
from PyQt5.QtCore import pyqtSignal, Qt
from cell_view import CellView

class GridView(QWidget):
    cell_toggled = pyqtSignal(int, int)

    def __init__(self, rows: int, cols: int):
        super().__init__()
        self.rows = rows
        self.cols = cols

        self.layout = QGridLayout()
        self.layout.setSpacing(0)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self.layout)

        self.cells = []
        for r in range(rows):
            row_cells = []
            for c in range(cols):
                cell = CellView(r, c)
                cell.clicked.connect(lambda _, r=r, c=c: self.cell_toggled.emit(r, c))
                self.layout.addWidget(cell, r, c)
                row_cells.append(cell)
            self.cells.append(row_cells)

    def update_cell(self, r: int, c: int, cell_type: str):
        self.cells[r][c].set_cell_type(cell_type)

    def refresh_grid(self):
        for row in self.cells:
            for cell in row:
                cell.update_style()

    def get_algorithm(self) -> str:
        return self.parent().settings_panel.algorithm_box.currentText()

    def get_heuristic(self) -> str:
        return self.parent().settings_panel.heuristic_box.currentText()

    def get_maze_method(self) -> str:
        return self.parent().settings_panel.maze_box.currentText()

    def get_speed(self) -> int:
        return self.parent().settings_panel.speed_slider.value()