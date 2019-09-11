import sys
from PyQt5.QtGui import QShowEvent
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QDesktopWidget, QApplication


class HelloWorldWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('HelloWorld')

        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addWidget(QLabel('Hello World'))
        vbox.addStretch(1)
        self.setLayout(vbox)

        self.setGeometry(300, 300, 640, 480)
        self.show()

    def showEvent(self, event: QShowEvent) -> None:
        rect = QDesktopWidget().screenGeometry(self)
        my = self.geometry()

        my.moveCenter(rect.center())
        self.setGeometry(my)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = HelloWorldWindow()
    sys.exit(app.exec_())
