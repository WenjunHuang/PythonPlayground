from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QWidget, QTableView, QVBoxLayout, QApplication


class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(300, 300, 400, 300)
        self.setWindowTitle("QTableView")

        self.initData()
        self.initUI()

    def initData(self):
        data = ("blue", "green", "yellow", "red")
        self.model = QStandardItemModel(10, 6)

        row = 0
        col = 0

        for i in data:
            item = QStandardItem(i)
            self.model.setItem(row, col, item)
            row = row + 1

    def initUI(self):
        self.tv = QTableView(self)
        self.tv.setModel(self.model)

        vbox = QVBoxLayout()
        vbox.addWidget(self.tv)
        self.setLayout(vbox)


import sys

app = QApplication(sys.argv)
ex = Example()
ex.show()
sys.exit(app.exec_())
