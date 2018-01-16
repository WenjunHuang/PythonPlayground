import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QLinearGradient, QPainter, qRgba, QColor, QBrush, QPaintEvent
from PyQt5.QtWidgets import QWidget, QApplication


class DrawGradients(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('DrawGradients')
        self.setGeometry(300, 300, 640, 480)

    def drawGradients(self, painter: QPainter):
        painter.setBackground(QBrush(Qt.cyan))
        painter.eraseRect(0, 0, self.width(), self.height())

        grad1 = QLinearGradient(0, 20, 0, 110)
        grad1.setColorAt(0.1, Qt.black)
        grad1.setColorAt(0.5, Qt.yellow)
        grad1.setColorAt(0.9, Qt.black)

        painter.fillRect(20, 20, 300, 90, grad1)

        grad2 = QLinearGradient(0, 55, 250, 0)
        grad2.setColorAt(0.2, Qt.black)
        grad2.setColorAt(0.5, Qt.red)
        grad2.setColorAt(0.8, Qt.black)

        painter.fillRect(20, 140, 300, 100, grad2)

        grad3 = QLinearGradient(0, 280, 0, 380)
        grad3.setColorAt(0.1, QColor(0xcc, 0xcc, 0xcc, 156))
        grad3.setColorAt(0.8, QColor(0xcc, 0xcc, 0xcc, 0))
        painter.fillRect(20, 280, 300, 100, grad3)

    def paintEvent(self, event: QPaintEvent):
        painter = QPainter()
        painter.begin(self)
        self.drawGradients(painter)
        painter.end()


app = QApplication([])
window = DrawGradients()
window.show()
sys.exit(app.exec_())
