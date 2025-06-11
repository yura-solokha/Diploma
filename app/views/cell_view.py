from PyQt5.QtWidgets import QPushButton
from PyQt5.QtCore import Qt

class CellView(QPushButton):
    def __init__(self, row: int, col: int):
        super().__init__()
        self.row = row
        self.col = col
        self.setFixedSize(25, 25)
        self.setProperty('cellType', 'default')
        self.update_style()

    def set_cell_type(self, cell_type: str):
        self.setProperty('cellType', cell_type)
        self.update_style()

    def update_style(self):
        self.style().unpolish(self)
        self.style().polish(self)
        self.repaint()