import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QPaintEvent
from PyQt5.QtWidgets import QWidget, QApplication


class DrawRectangles(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("draw rectanges")
        self.setGeometry(200, 200, 480, 360)

    def drawRectangles(self, painter: QPainter) -> None:
        for i in range(1, 11):
            painter.setOpacity(i * 0.1)
            painter.fillRect(50 * i, 20, 40, 40, Qt.darkGray)

    def paintEvent(self, event: QPaintEvent) -> None:
        painter = QPainter()
        painter.begin(self)
        self.drawRectangles(painter)
        painter.end()


app = QApplication([])
window = DrawRectangles()
window.show()
sys.exit(app.exec_())
