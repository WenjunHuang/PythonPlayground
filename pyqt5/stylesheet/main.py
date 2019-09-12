import sys

from PyQt5.QtWidgets import QApplication
from main_window import MainWindow
import stylesheet_rc

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.setGeometry(300,300,640,480)
    window.show()
    sys.exit(app.exec_())
