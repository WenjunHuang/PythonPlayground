from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QFrame, QGridLayout, QWidget, QVBoxLayout, QRadioButton, QComboBox, QLabel, \
    QLineEdit, QSpinBox, QSpacerItem, QSizePolicy, QDialogButtonBox, QListWidget, QCheckBox, QAction


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.initMenuBarAndStatusBar()

    def initMenuBarAndStatusBar(self):
        exitAction = QAction('&Exit', self)
        aboutQtAction = QAction('Abount Qt', self)
        editStyleAction = QAction("Edit &Style...", self)
        aboutAction = QAction("About", self)

        menu_bar = self.menuBar()

        file_menu = menu_bar.addMenu("&File")
        file_menu.addAction(editStyleAction)
        file_menu.addSeparator()
        file_menu.addAction(exitAction)

        help_menu = menu_bar.addMenu("&Help")
        help_menu.addAction(aboutAction)
        help_menu.addAction(aboutQtAction)

    def initUI(self):
        frame = QFrame(self, frameShape=QFrame.StyledPanel, frameShadow=QFrame.Raised)
        gridLayout = QGridLayout()
        gridLayout.setSpacing(6)
        gridLayout.setContentsMargins(9, 9, 9, 9)
        frame.setLayout(gridLayout)

        self.nameCombo = QComboBox(self, toolTip="Specify your name", editable=True)
        self.nameLabel = QLabel("&Name", self, alignment=Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)
        self.nameLabel.setBuddy(self.nameCombo)
        gridLayout.addWidget(self.nameLabel, 0, 0, 1, 1)
        gridLayout.addWidget(self.nameCombo, 0, 1, 1, 4)

        self.maleRadioButton = QRadioButton(self, text="&Male", toolTip="Check this if you are mail")
        gridLayout.addWidget(self.maleRadioButton, 1, 1, 1, 1)
        self.femaleRadioButton = QRadioButton(self, text="&Female", toolTip='Check this if you are female')
        gridLayout.addWidget(self.femaleRadioButton, 1, 2, 1, 2)

        self.genderLabel = QLabel('Gender:', self,
                                  alignment=Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)
        gridLayout.addWidget(self.genderLabel, 1, 0, 1, 1)
        gridLayout.addItem(QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum), 1, 4)

        self.ageSpinBox = QSpinBox(self,
                                   toolTip="Specify your age",
                                   statusTip="Specify your age",
                                   minimum=12,
                                   value=22)
        gridLayout.addWidget(self.ageSpinBox, 2, 1, 1, 2)
        self.ageLabel = QLabel('&Age:', self, alignment=Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)
        self.ageLabel.setBuddy(self.ageSpinBox)
        gridLayout.addWidget(self.ageLabel, 2, 0, 1, 1)
        gridLayout.addItem(QSpacerItem(61, 20, QSizePolicy.Expanding, QSizePolicy.Minimum), 2, 3, 1, 2)

        self.passwordEdit = QLineEdit('Password:', self, toolTip='Specify your password',
                                      statusTip='Specify your password',
                                      echoMode=QLineEdit.Password)
        gridLayout.addWidget(self.passwordEdit, 3, 1, 1, 4)

        self.passwordLabel = QLabel('&Password:', self, alignment=Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)
        self.passwordLabel.setBuddy(self.passwordEdit)
        gridLayout.addWidget(self.passwordLabel, 3, 0, 1, 1)

        self.countryCombo = QComboBox(self, toolTip='Specify country of origin',
                                      statusTip='Specify country of origin')
        self.countryCombo.addItems(['Egypt', 'France', 'Germany', 'India', 'Italy', 'Norway', 'Pakistan', ])
        self.countryCombo.setCurrentIndex(6)
        gridLayout.addWidget(self.countryCombo, 4, 1, 1, 4)
        self.countryLabel = QLabel('Country:', self,
                                   alignment=Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)
        self.countryLabel.setBuddy(self.countryCombo)
        gridLayout.addWidget(self.countryLabel, 4, 0, 1, 1)

        self.professionList = QListWidget(self,
                                          toolTip='Select your profession',
                                          statusTip='Specify your name here')
        self.professionList.addItems(['Developer', 'Student', 'Fisherman'])
        self.professionListLabel = QLabel('Profession:', self,
                                          alignment=Qt.AlignRight | Qt.AlignTop | Qt.AlignTrailing)
        self.professionListLabel.setBuddy(self.professionList)
        gridLayout.addWidget(self.professionListLabel, 5, 0, 1, 1)
        gridLayout.addWidget(self.professionList, 5, 1, 1, 4)

        self.agreeCheckBox = QCheckBox('I accept the terms and &conditions', self,
                                       toolTip='Please read the LICENSE file before checking')
        gridLayout.addWidget(self.agreeCheckBox, 6, 0, 1, 5)

        self.buttonBox = QDialogButtonBox(self, orientation=Qt.Horizontal,
                                          standardButtons=QDialogButtonBox.Cancel | QDialogButtonBox.Ok)
        gridLayout.addWidget(self.buttonBox, 7, 3, 1, 2)

        center = QWidget()
        vlayout = QVBoxLayout()
        vlayout.addWidget(frame)
        center.setLayout(vlayout)
        self.setCentralWidget(center)
