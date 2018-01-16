import sys
from PyQt5.QtCore import Qt

from PyQt5.QtGui import QPainter, QRadialGradient, QPaintEvent
from PyQt5.QtWidgets import QWidget, QApplication


class DrawRadialGradients(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Draw Radial Gradients')
        self.setGeometry(300, 300, 480, 360)

    def drawGradients(self, painter: QPainter):
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setPen(Qt.NoPen)

        gr1 = QRadialGradient(20.0, 20.0, 110.0)
        painter.setBrush(gr1)
        painter.drawEllipse(20.0, 20.0, 100.0, 100.0)

        gr2 = QRadialGradient(190.0, 70.0, 50.0, 190.0, 70.0)
        gr2.setColorAt(0.2, Qt.yellow)
        gr2.setColorAt(0.7, Qt.black)
        painter.setBrush(gr2)
        painter.drawEllipse(140.0, 20.0, 100.0, 100.0)

    def paintEvent(self, event:QPaintEvent):
        painter = QPainter()
        painter.begin(self)
        self.drawGradients(painter)
        painter.end()

app = QApplication([])
window = DrawRadialGradients()
window.show()
sys.exit(app.exec_())
