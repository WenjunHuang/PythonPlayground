import sys
from PySide2.QtWidgets import *
from PySide2.QtGui import *


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        QToolTip.setFont(QFont('Mono', 20))
        QToolTip.setPalette(QPalette(QColor(0, 255, 0)))
        self.setToolTip('This is a <b>QWidget</b> widget')

        btn = QPushButton('Button', self)
        btn.setToolTip('This is a <b>QPushButton</b> widget')
        btn.resize(btn.sizeHint())
        btn.move(50, 50)
        self.resize(250, 150)
        self.center()
        self.setWindowTitle('Tooltips')

        self.show()

    def center(self) -> None:
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def closeEvent(self, event: QCloseEvent) -> None:
        reply = QMessageBox.question(self,
                                     'Message',
                                     'Are your sure to quit?',
                                     QMessageBox.Yes | QMessageBox.No,
                                     QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


def main():
    app = QApplication(sys.argv)

    ex = Example()

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
