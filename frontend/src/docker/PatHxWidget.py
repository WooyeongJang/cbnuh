from PyQt5.QtWidgets import QWidget, QTextEdit


class PatHxWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.wg = QTextEdit(self)
