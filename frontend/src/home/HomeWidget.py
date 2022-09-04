from PyQt5.QtWidgets import QWidget, QLabel
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QLabel, QFrame, QPushButton, QListWidget
from PyQt5 import QtCore

import sys

class HomeWidget(QWidget):
    def __init__(self):
        super().__init__()
        #
        self.layout = QHBoxLayout()

        # creating label
        self.layout_left = QLabel()
        self.layout_left.setAlignment(Qt.AlignCenter)

        # loading image
        self.pixmap = QPixmap('/home/wyjang/IdeaProjects/cbnuh/frontend/src/home/home.png')
        w = self.layout_left.width()
        h = self.layout_left.height()
        pixmap_resized = self.pixmap.scaled(w*2.8, h*1.8)

        # adding image to label
        self.layout_left.setPixmap(pixmap_resized)

        # self.layout.addWidget(self.layout_right)
        self.layout.addWidget(self.layout_left)
        # self.layout.addLayout(self.layout_right)
        self.setLayout(self.layout)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    m = HomeWidget()
    m.showMaximized()
    sys.exit(app.exec_())