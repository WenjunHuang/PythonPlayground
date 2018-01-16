from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter, QFont
import sys

lyrics = [
    "Most relationships seem so transitory",
    "They're all good but not the permanent one",
    "Who doesn't long for someone to hold",
    "Who knows how to love without being told",
    "Somebody tell me why I'm on my own",
    "If there's a soulmate for everyone"
]


class DrawText(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 430, 240)
        self.setWindowTitle('Soulmate')
        self.show()

    def paintEvent(self, event):
        painter = QPainter()
        painter.begin(self)
        self.drawLyrics(painter)
        painter.end()

    def drawLyrics(self, painter):
        painter.setFont(QFont('Zapfino', 11))
        painter.drawText(20, 30, lyrics[0])
        painter.drawText(20, 60, lyrics[1])
        painter.drawText(20, 120, lyrics[2])
        painter.drawText(20, 150, lyrics[3])
        painter.drawText(20, 180, lyrics[4])
        painter.drawText(20, 210, lyrics[5])

app = QApplication([])
ex = DrawText()
sys.exit(app.exec_())
