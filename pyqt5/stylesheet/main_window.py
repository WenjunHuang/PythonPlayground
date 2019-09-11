from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QFrame, QGridLayout, QWidget, QVBoxLayout, QRadioButton, QComboBox, QLabel, \
    QLineEdit


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        frame = QFrame(self, frameShape=QFrame.StyledPanel, frameShadow=QFrame.Raised)
        gridLayout = QGridLayout()
        frame.setLayout(gridLayout)

        self.nameCombo = QComboBox(self, toolTip="Specify your name", editable=True)
        gridLayout.addWidget(self.nameCombo, 0, 1, 1, 4)
        self.maleRadioButton = QRadioButton(self, text="&Male", toolTip="Check this if you are mail")
        gridLayout.addWidget(self.maleRadioButton, 1, 1, 1, 1)

        self.passwordEdit = QLineEdit('Password', self, toolTip='Specify your password',
                                      statusTip='Specify your password',
                                      echoMode=QLineEdit.Password)
        gridLayout.addWidget(self.passwordEdit, 3, 1, 1, 4)

        self.passwordLabel = QLabel('&Password', self, alignment=Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)
        self.passwordLabel.setBuddy(self.passwordEdit)
        gridLayout.addWidget(self.passwordLabel, 3, 0, 1, 1)

        self.countryCombo = QComboBox(self, toolTip='Specify country of origin',
                                      statusTip='Specify country of origin')
        self.countryCombo.addItems(['Egypt', 'France', 'Germany', 'India', 'Italy', 'Norway', 'Pakistan', ])
        self.countryCombo.setCurrentIndex(6)
        gridLayout.addWidget(self.countryCombo, 4, 1, 1, 4)

        center = QWidget()
        vlayout = QVBoxLayout()
        vlayout.addWidget(frame)
        center.setLayout(vlayout)
        self.setCentralWidget(center)
