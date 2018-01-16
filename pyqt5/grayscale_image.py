from PyQt5.QtWidgets import QWidget,QApplication
from PyQt5.QtGui import QPainter,QImage,qGray,qAlpha,qRgba
import sys

class GrayScale(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.sid = QImage("smallsid.jpg")
        self.w = self.sid.width()
        self.h = self.sid.height()
        self.setGeometry(200,200,320,150)
        self.setWindowTitle('Sid')
        self.show()
    def paintEvent(self,event):
        painter = QPainter()
        painter.begin(self)
        self.drawImages(painter)
        painter.end()
    def grayScale(self,image):
        for i in range(self.w):
            for j in range(self.h):
                c = image.pixel(i,j)
                gray = qGray(c)
                alpha = qAlpha(c)
                image.setPixel(i,j,qRgba(gray,gray,gray,alpha))
        return image
    def drawImages(self, painter):
        painter.drawImage(5,15,self.sid)
        painter.drawImage(self.w + 10,15,
                          self.grayScale(self.sid.copy()))

app = QApplication([])
ex = GrayScale()
sys.exit(app.exec_())