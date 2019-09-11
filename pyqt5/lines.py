from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPaintEvent, QPainter, QMouseEvent, QColor
from PyQt5.QtWidgets import QWidget, QApplication


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

    def paintEvent(self, event: QPaintEvent) -> None:
        painter = QPainter()
        painter.begin(self)
        self.draw_lines(painter)
        painter.end()

    def mousePressEvent(self, event: QMouseEvent) -> None:
        if event.button() == Qt.LeftButton:
            x = event.x()
            y = event.y()

            self.cs[self.count][0] = x
            self.cs[self.count][1] = y
            self.count = self.count + 1
            self.repaint()

        if event.button() == Qt.RightButton:
            self.count = 0
            self.repaint()

    def draw_lines(self, painter: QPainter):
        painter.save()
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setPen(QColor(255, 0, 0))
        w = self.width()
        h = self.height()

        painter.eraseRect(0, 0, w, h)

        for i in range(self.count):
            for j in range(self.count):
                painter.drawLine(self.cs[i][0],
                                 self.cs[i][1],
                                 self.cs[j][0],
                                 self.cs[j][1])

        painter.restore()


import sys

app = QApplication(sys.argv)
ex = Example()
sys.exit(app.exec_())
