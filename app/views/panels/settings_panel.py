from PyQt5.QtWidgets import QWidget, QVBoxLayout, QGroupBox, QComboBox, QLabel, QSlider
from PyQt5.QtCore import pyqtSignal, Qt

class SettingsPanel(QWidget):
    speed_changed = pyqtSignal(int)

    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()

        algo_group = QGroupBox("Алгоритм пошуку")
        algo_layout = QVBoxLayout()
        self.algorithm_box = QComboBox()
        self.algorithm_box.addItems(["Алгоритм A*", "Алгоритм Дейкстри", "Пошук в ширину (BFS)", "Пошук в глибину (DFS)", "Жадібний пошук"])
        algo_layout.addWidget(self.algorithm_box)
        algo_group.setLayout(algo_layout)
        layout.addWidget(algo_group)

        heur_group = QGroupBox("Евристика")
        heur_layout = QVBoxLayout()
        self.heuristic_box = QComboBox()
        self.heuristic_box.addItems(["Мангеттен","Евклідова","Чебишева","Октильна"])
        heur_layout.addWidget(self.heuristic_box)
        heur_group.setLayout(heur_layout)
        layout.addWidget(heur_group)

        maze_group = QGroupBox("Генерація лабіринту")
        maze_layout = QVBoxLayout()
        self.maze_box = QComboBox()
        self.maze_box.addItems(["Прим", "Рекурсивне відстеження", "Рекурсивний поділ"])
        maze_layout.addWidget(self.maze_box)
        maze_group.setLayout(maze_layout)
        layout.addWidget(maze_group)

        layout.addWidget(QLabel("Швидкість (мс)"))
        self.speed_slider = QSlider(Qt.Horizontal)
        self.speed_slider.setRange(1, 100)
        self.speed_slider.setValue(50)
        self.speed_slider.valueChanged.connect(lambda v: self.speed_changed.emit(v))
        layout.addWidget(self.speed_slider)
        layout.addStretch()
        self.setLayout(layout)


