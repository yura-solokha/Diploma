from PyQt5.QtWidgets import QMainWindow, QWidget, QHBoxLayout, QVBoxLayout
from controllers.grid_controller import GridController
from models.grid_model import GridModel
from views.panels.control_panel import ControlPanel
from views.panels.settings_panel import SettingsPanel
from views.panels.stats_panel import StatsPanel
from views.grid_view import GridView

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Візуалізація пошуку шляху")
        self.setGeometry(100, 100, 1000, 800)

        self.model = GridModel(rows=30, cols=30)
        self.view = QWidget()
        self.setCentralWidget(self.view)

        main_layout = QVBoxLayout()
        self.view.setLayout(main_layout)

        top_layout = QHBoxLayout()
        self.control_panel = ControlPanel()
        self.settings_panel = SettingsPanel()
        top_layout.addWidget(self.control_panel)
        top_layout.addWidget(self.settings_panel)
        main_layout.addLayout(top_layout)

        content_layout = QHBoxLayout()
        self.grid_view = GridView(rows=30, cols=30)
        self.stats_panel = StatsPanel()
        content_layout.addWidget(self.grid_view, 4)
        content_layout.addWidget(self.stats_panel, 1)
        main_layout.addLayout(content_layout)

        self.controller = GridController(model=self.model, view=self.grid_view)
        self.control_panel.run_clicked.connect(self.controller.on_run_clicked)
        self.control_panel.generate_clicked.connect(self.controller.on_generate_clicked)
        self.settings_panel.speed_changed.connect(self.controller.on_speed_changed)
        self.stats_panel.clear_grid_clicked.connect(self.controller.on_clear_grid)
        self.stats_panel.clear_path_clicked.connect(self.controller.on_clear_path)
        self.stats_panel.stop_animation_clicked.connect(self.controller.on_stop_animation)
        self.grid_view.cell_toggled.connect(self.controller.on_cell_toggled)

