from PyQt5.QtWidgets import QWidget, QPushButton, QHBoxLayout
from PyQt5.QtCore import pyqtSignal

class ControlPanel(QWidget):
    run_clicked = pyqtSignal()
    generate_clicked = pyqtSignal()

    def __init__(self):
        super().__init__()
        layout = QHBoxLayout()
        self.run_btn = QPushButton("Запустити пошук")
        self.gen_btn = QPushButton("Згенерувати лабіринт")
        layout.addWidget(self.run_btn)
        layout.addWidget(self.gen_btn)
        self.setLayout(layout)

        self.run_btn.clicked.connect(lambda: self.run_clicked.emit())
        self.gen_btn.clicked.connect(lambda: self.generate_clicked.emit())

