from PyQt5.QtWidgets import QWidget, QVBoxLayout, QGroupBox, QLabel, QPushButton
from PyQt5.QtCore import pyqtSignal

class StatsPanel(QWidget):
    clear_grid_clicked = pyqtSignal()
    clear_path_clicked = pyqtSignal()
    stop_animation_clicked = pyqtSignal()

    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()

        stats_group = QGroupBox("Статистика")
        stats_layout = QVBoxLayout()
        self.time_label = QLabel("Час (мс): -")
        self.visited_label = QLabel("Відвідано: -")
        self.path_label = QLabel("Довжина: -")
        stats_layout.addWidget(self.time_label)
        stats_layout.addWidget(self.visited_label)
        stats_layout.addWidget(self.path_label)
        stats_group.setLayout(stats_layout)
        layout.addWidget(stats_group)

        self.clear_btn = QPushButton("Очистити сітку")
        self.clear_path_btn = QPushButton("Очистити маршрут")
        self.stop_btn = QPushButton("Зупинити анімацію")
        layout.addWidget(self.clear_btn)
        layout.addWidget(self.clear_path_btn)
        layout.addWidget(self.stop_btn)
        layout.addStretch()
        self.setLayout(layout)

        self.clear_btn.clicked.connect(lambda: self.clear_grid_clicked.emit())
        self.clear_path_btn.clicked.connect(lambda: self.clear_path_clicked.emit())
        self.stop_btn.clicked.connect(lambda: self.stop_animation_clicked.emit())

