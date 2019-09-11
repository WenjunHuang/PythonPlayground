from PyQt5.QtCore import QStringListModel
from PyQt5.QtWidgets import QWidget, QListView, QVBoxLayout, QApplication


class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(300, 3003, 350, 300)
        self.setWindowTitle("QListView")

        self.initData()
        self.initUI()

    def initData(self):
        names = ["Jack", "Tom", "Lucy", "Bill", "Jane"]
        self.model = QStringListModel(names)

    def initUI(self):
        lv = QListView(self)
        lv.setModel(self.model)

        layout = QVBoxLayout()
        layout.addWidget(lv)
        self.setLayout(layout)


import sys

app = QApplication(sys.argv)
ex = Example()
ex.show()
sys.exit(app.exec_())
