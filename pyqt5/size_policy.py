from PyQt5.QtWidgets import QWidget, QPushButton, QSizePolicy, QHBoxLayout, QApplication


class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        btn1 = QPushButton("Button", self)
        # btn1.setSizePolicy(QSizePolicy.Fixed,
        #                    QSizePolicy.Fixed)

        btn2 = QPushButton("Button", self)
        btn3 = QPushButton("Button", self)
        # btn3.setSizePolicy(QSizePolicy.Fixed,
        #                    QSizePolicy.Fixed)

        layout = QHBoxLayout()
        layout.addWidget(btn1)
        layout.addWidget(btn2)
        layout.addWidget(btn3)

        self.setLayout(layout)

        self.setGeometry(300, 300, 250, 150)
        self.show()


import sys

app = QApplication(sys.argv)
ex = Example()
sys.exit(app.exec_())
