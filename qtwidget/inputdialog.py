import sys

from PyQt5.QtWidgets import QWidget, QPushButton, QLineEdit


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.btn = QPushButton('Dialog',self)
        self.btn.move(20,20)
        self.btn.clicked.connect(self.showDialog)

        self.le = QLineEdit(self)
        self.le.move(130,22)

        self.setGeometry(300,300,290,150)
        self.setWindowTitle('Input dialog')