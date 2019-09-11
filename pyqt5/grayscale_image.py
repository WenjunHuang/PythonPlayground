from PyQt5.QtGui import QImage, QPaintEvent, QPainter, qGray, qAlpha, qRgba
from PyQt5.QtWidgets import QWidget, QApplication
import grayscale_image_res


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.sid = QImage(":/images/smallsid")
        self.w = self.sid.width()
        self.h = self.sid.height()

        self.setGeometry(200, 200, 320, 150)
        self.setWindowTitle('Sid')
        self.show()

    def paintEvent(self, event: QPaintEvent) -> None:
        painter = QPainter()
        painter.begin(self)
        self.draw_images(painter)
        painter.end()

    def gray_scale(self, image: QImage):
        for i in range(self.w):
            for j in range(self.h):
                c = image.pixel(i, j)
                gray = qGray(c)
                alpha = qAlpha(c)
                image.setPixel(i, j, qRgba(gray, gray, gray, alpha))
        return image

    def draw_images(self, painter: QPainter):
        painter.drawImage(5, 15, self.sid)
        painter.drawImage(self.w + 10, 15,
                          self.gray_scale(self.sid.copy()))


import sys

app = QApplication(sys.argv)
ex = Example()
sys.exit(app.exec_())
