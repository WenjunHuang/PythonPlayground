from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QComboBox, QGroupBox, QCheckBox, QPushButton, \
    QApplication


class FindReplace(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        vbox = QVBoxLayout()

        hbox1 = QHBoxLayout()
        hbox1.addWidget(QLabel("Find"))
        hbox1.addWidget(QComboBox())

        vbox.addLayout(hbox1)

        hbox2 = QHBoxLayout()
        hbox2.addWidget(QLabel("Replace with"))
        hbox2.addWidget(QComboBox())

        vbox.addLayout(hbox2)

        hbox3 = QHBoxLayout()

        direction = QGroupBox("Direction")
        dirvbox = QVBoxLayout()
        dirvbox.addWidget(QCheckBox("Forward"))
        dirvbox.addWidget(QCheckBox("Backward"))
        direction.setLayout(dirvbox)

        hbox3.addWidget(direction)

        scope = QGroupBox("Scope")
        scvbox = QVBoxLayout()
        scvbox.addWidget(QCheckBox("All"))
        scvbox.addWidget(QCheckBox("Selected items"))

        scope.setLayout(scvbox)

        hbox3.addWidget(scope)
        vbox.addLayout(hbox3)

        options = QGroupBox("Options")
        opthbox = QHBoxLayout()
        optvbox1 = QVBoxLayout()
        optvbox2 = QVBoxLayout()

        optvbox1.addWidget(QCheckBox("Case Sensitive"))
        optvbox2.addWidget(QCheckBox("Whole word"))
        regex = QCheckBox("Regular expressions")
        optvbox1.addWidget(regex)
        optvbox2.addWidget(QCheckBox("Wrap search"))
        optvbox2.addWidget(QCheckBox("Incremental"))
        opthbox.addLayout(optvbox1)
        opthbox.addLayout(optvbox2)
        options.setLayout(opthbox)

        vbox.addWidget(options)

        hbox4 = QHBoxLayout()
        hbox4.addWidget(QPushButton("Find"))
        hbox4.addWidget(QPushButton("Find/Replace"))

        vbox.addLayout(hbox4)

        hbox5 = QHBoxLayout()
        hbox5.addWidget(QPushButton("Replace"))
        hbox5.addWidget(QPushButton("Replace All"))

        vbox.addLayout(hbox5)

        hbox6 = QHBoxLayout()
        hbox6.addStretch(1)
        hbox6.addWidget(QPushButton("Close"))
        vbox.addLayout(hbox6)

        self.setLayout(vbox)
        self.show()


import sys

app = QApplication(sys.argv)
ex = FindReplace()
sys.exit(app.exec_())
