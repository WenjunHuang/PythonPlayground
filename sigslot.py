import sys

from PySide2.QtCore import Qt, Signal, Slot
from PySide2.QtWidgets import *


class Example(QWidget):
    time = Signal(str)

    @Slot(str)
    def slideChange(self, value: str):
        totalSeconds = int(value)
        minutes = totalSeconds // 60
        seconds = totalSeconds - minutes * 60

        self.time.emit("%02d:%02d" % (minutes, seconds))

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        lcd = QLCDNumber(self)
        sld = QSlider(Qt.Horizontal, self)
        sld.setRange(0, 9999)

        vbox = QVBoxLayout()
        vbox.addWidget(lcd)
        vbox.addWidget(sld)

        self.setLayout(vbox)
        sld.valueChanged.connect(self.slideChange)
        self.time.connect(lcd.display)

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Signal and slot')
        self.show()


app = QApplication(sys.argv)
ex = Example()
sys.exit(app.exec_())
