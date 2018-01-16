from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter
from PyQt5.QtCore import Qt
import sys


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.cs = [[0 for i in range(2)] for j in range(100)]
        self.count = 0
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Lines')
        self.show()

    def paintEvent(self, event):
        painter = QPainter()
        painter.begin(self)
        self.drawLines(painter)
        painter.end()

    def mousePressEvent(self, e):
        if e.button() == Qt.LeftButton:
            x = e.x()
            y = e.y()
            self.cs[self.count][0] = x
            self.cs[self.count][1] = y
            self.count = self.count + 1
        if e.button() == Qt.RightButton:
            self.repaint()
            self.count = 0

    def drawLines(self, painter):
        painter.setRenderHint(QPainter.Antialiasing)
        w = self.width()
        h = self.height()
        painter.eraseRect(0, 0, w, h)

        for i in range(self.count):
            for j in range(self.count):
                painter.drawLine(self.cs[i][0], self.cs[i][1], self.cs[j][0], self.cs[j][1])

app = QApplication([])
ex = Example()
sys.exit(app.exec_())
