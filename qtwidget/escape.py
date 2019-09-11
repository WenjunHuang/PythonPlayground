import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QKeyEvent, QCloseEvent


class Example(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.initUI()

    def initUI(self) -> None:
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle("Event handler")
        self.show()

    def keyPressEvent(self, event: QKeyEvent) -> None:
        if event.key() == Qt.Key_Escape:
            self.close()

    def closeEvent(self, event: QCloseEvent) -> None:
        print("close event")
        super().closeEvent(event)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
