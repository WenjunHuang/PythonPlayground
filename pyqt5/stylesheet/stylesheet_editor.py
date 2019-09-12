from PyQt5.QtCore import Qt, pyqtSlot, QFile
from PyQt5.QtWidgets import QDialog, QGridLayout, QSpacerItem, QSizePolicy, QLabel, QComboBox, QTextEdit, QHBoxLayout, \
    QPushButton, QApplication, QStyleFactory, qApp
import re


class StyleSheetEditor(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.initUI()

        reg_exp = r"^.(.*)\+?Style$"
        default_style = QApplication.style().metaObject().className()
        match = re.match(reg_exp, default_style)
        if match:
            default_style = match[1]
        self.styleCombo.addItems(QStyleFactory.keys())
        self.styleCombo.setCurrentIndex(self.styleCombo.findText(default_style,
                                                                 Qt.MatchContains))

    def initUI(self):
        self.setWindowTitle('Style Editor')
        self.setObjectName('StyleSheetEditor')
        self.resize(445, 289)

        gridLayout = QGridLayout(self)
        gridLayout.setObjectName('gridLayout')
        gridLayout.setSpacing(6)
        gridLayout.setContentsMargins(9, 9, 9, 9)

        gridLayout.addItem(QSpacerItem(32, 20,
                                       QSizePolicy.MinimumExpanding,
                                       QSizePolicy.Minimum),
                           0, 0, 1, 1)

        sp = QSizePolicy(
            QSizePolicy.Fixed,
            QSizePolicy.Preferred
        )
        sp.setHorizontalStretch(0)
        sp.setVerticalStretch(0)
        gridLayout.addWidget(QLabel('Style:', self,
                                    sizePolicy=sp), 0, 1, 1, 1)

        sp = QSizePolicy(
            QSizePolicy.Preferred,
            QSizePolicy.Fixed,
        )
        sp.setHorizontalStretch(0)
        sp.setVerticalStretch(0)
        self.styleCombo = QComboBox()
        sp.setHeightForWidth(self.styleCombo.sizePolicy().hasHeightForWidth())
        self.styleCombo.setSizePolicy(sp)
        gridLayout.addWidget(self.styleCombo, 0, 2, 1, 1)

        gridLayout.addItem(QSpacerItem(10,
                                       16,
                                       QSizePolicy.Fixed,
                                       QSizePolicy.Minimum),
                           0, 3, 1, 1)

        sp = QSizePolicy(QSizePolicy.Fixed,
                         QSizePolicy.Preferred)
        sp.setHorizontalStretch(0)
        sp.setVerticalStretch(0)
        gridLayout.addWidget(QLabel('Style Sheet:', sizePolicy=sp),
                             0, 4, 1, 1)

        self.styleSheetCombo = QComboBox()
        self.styleSheetCombo.addItems(['Default', 'Coffee', 'Pagefold', ])
        gridLayout.addWidget(self.styleSheetCombo, 0, 5, 1, 1)

        gridLayout.addItem(QSpacerItem(32, 20, QSizePolicy.MinimumExpanding, QSizePolicy.Minimum),
                           0,
                           6,
                           1,
                           1)

        self.styleTextEdit = QTextEdit(self)
        self.styleTextEdit.setObjectName('styleTextEdit')
        gridLayout.addWidget(self.styleTextEdit, 1, 0, 1, 7)

        self.hboxLayout = QHBoxLayout()
        self.hboxLayout.setSpacing(6)
        self.hboxLayout.setContentsMargins(0, 0, 0, 0)
        self.hboxLayout.setObjectName('hboxLayout')
        self.hboxLayout.addItem(QSpacerItem(321, 20, QSizePolicy.Expanding, QSizePolicy.Minimum))
        self.applyButton = QPushButton('&Apply', self)
        self.applyButton.setEnabled(False)
        self.hboxLayout.addWidget(self.applyButton)
        gridLayout.addLayout(self.hboxLayout, 2, 0, 1, 7)

        self.styleCombo.activated[str].connect(self.on_styleCombo_activated)
        self.styleSheetCombo.activated[str].connect(self.on_styleSheetCombo_activated)
        self.styleTextEdit.textChanged.connect(self.on_styleTextEdit_textChanged)
        self.applyButton.clicked.connect(self.on_applyButton_clicked)

    def on_applyButton_clicked(self):
        qApp.setStyleSheet(self.styleTextEdit.toPlainText())
        self.applyButton.setEnabled(False)

    def on_styleTextEdit_textChanged(self):
        self.applyButton.setEnabled(True)

    @pyqtSlot(str)
    def on_styleCombo_activated(self, style_name: str):
        print(style_name)
        qApp.setStyle(style_name)
        self.applyButton.setEnabled(False)

    def on_styleSheetCombo_activated(self,sheet_name:str):
        self.load_stylesheet(sheet_name)

    def load_stylesheet(self, sheet_name: str):
        file = QFile(f":/styles/{sheet_name.lower()}.css")
        file.open(QFile.ReadOnly)
        style_sheet = str(file.readAll(), encoding='utf-8')

        self.styleTextEdit.setPlainText(style_sheet)
        qApp.setStyleSheet(style_sheet)
        self.applyButton.setEnabled(False)
