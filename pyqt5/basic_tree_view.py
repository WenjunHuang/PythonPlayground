from PyQt5.QtCore import QDir
from PyQt5.QtWidgets import QFileSystemModel, QTreeView, QVBoxLayout, QWidget, QApplication


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.model = QFileSystemModel()
        homedir = QDir.home().path()
        self.model.setRootPath(homedir)

        tv = QTreeView(self)
        tv.setModel(self.model)

        layout = QVBoxLayout()
        layout.addWidget(tv)
        self.setLayout(layout)
        self.show()


import sys

app = QApplication(sys.argv)
ex = Example()
sys.exit(app.exec_())
