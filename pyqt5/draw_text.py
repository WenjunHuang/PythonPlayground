import sys
import os

from PyQt5.QtGui import QPaintEvent, QPainter, QFont, QFontDatabase
from PyQt5.QtWidgets import QWidget, QApplication
import draw_text_res

lyrics = [
    "Most relationships seem so transitory", "They’re all good but not the permanent one",
    "Who doesn’t long for someone to hold",
    "Who knows how to love without being told", "Somebody tell me why I’m on my own",
    "If there’s a soulmate for everyone"
]


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 430, 240)
        self.setWindowTitle('Soulmate')
        self.show()

    def paintEvent(self, event: QPaintEvent) -> None:
        painter = QPainter()
        painter.begin(self)
        self.draw_lyrics(painter)
        painter.end()

    def draw_lyrics(self, painter: QPainter) -> None:
        painter.setFont(QFont('Chilanka', 20))
        painter.drawText(20, 30, lyrics[0])
        painter.drawText(20, 60, lyrics[1])
        painter.drawText(20, 120, lyrics[2])
        painter.drawText(20, 150, lyrics[3])
        painter.drawText(20, 180, lyrics[4])
        painter.drawText(20, 210, lyrics[5])


app = QApplication(sys.argv)
result = QFontDatabase.addApplicationFont(":/fonts/chilanka")
if result == -1:
    print('can not load font')

ex = Example()
sys.exit(app.exec_())
