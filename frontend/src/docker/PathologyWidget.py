from PyQt5.QtWidgets import QWidget, QTextEdit


class PathologyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.wg = QTextEdit(self)