from PyQt5.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QPushButton, QLabel, QGridLayout
from PyQt5.QtGui import QPixmap

class PatWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.layout = QGridLayout()
        self.left_layout = QVBoxLayout()
        self.left_widget_1 = QPushButton('Patient', self)
        self.left_widget_2 = QPushButton('Image', self)
        self.left_widget_3 = QPushButton('Pathology', self)
        self.left_widget_4 = QPushButton('History', self)
        self.left_widget_5 = QPushButton('RT-Plan', self)
        self.left_layout.addWidget(self.left_widget_1, 1)
        self.left_layout.addWidget(self.left_widget_2, 1)
        self.left_layout.addWidget(self.left_widget_3, 1)
        self.left_layout.addWidget(self.left_widget_4, 1)
        self.left_layout.addWidget(self.left_widget_5, 1)
        self.left_layout.addStretch()

        self.right_layout = QHBoxLayout()
        self.right_widget_1 = QLabel()

        self.right_widget_1.setPixmap(QPixmap("/home/wyjang/IdeaProjects/cbnuh/frontend/ref/prostate0017.png"))
        self.right_layout.addWidget(self.right_widget_1)

        self.layout.addLayout(self.left_layout, 0, 0)
        self.layout.addLayout(self.right_layout, 0, 1)

        self.setLayout(self.layout)
