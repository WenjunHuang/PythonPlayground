from PyQt5.QtCore import QSize, QObject
from PyQt5.QtWidgets import QPushButton, QWidget, QApplication, QVBoxLayout, QHBoxLayout


class MyButton(QPushButton):
    def __init__(self, text: str, parent: QWidget, size: QSize):
        super().__init__(text, parent)

        self.size = size

    def sizeHint(self) -> QSize:
        return self.size


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(300, 300, 300, 230)
        self.setWindowTitle("Size hints")

        self.initUI()

    def initUI(self):
        button1 = QPushButton("Button", self)
        # button1.move(20, 50)
        button2 = MyButton("Button", self, QSize(140, 27))
        # button2.move(150, 50)

        button3 = MyButton("Button", self, QSize(150, 60))
        button3.setMaximumSize(350, 60)
        button3.setMinimumSize(15, 60)
        # button3.move(50, 150)

        vbox = QHBoxLayout()
        vbox.addWidget(button1)
        vbox.addWidget(button2)
        vbox.addWidget(button3)
        self.setLayout(vbox)


import sys

app = QApplication(sys.argv)
ex = Example()
ex.show()
sys.exit(app.exec_())
