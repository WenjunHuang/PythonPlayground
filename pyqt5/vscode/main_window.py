from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, QSplitter, QListView, QTreeView, QTextEdit, QVBoxLayout, QApplication, \
    QToolBar, QAction
import vscode_rc


def read_style(file: str):
    with open(file, 'r') as f:
        return f.read()


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initToolbar(self):
        leftToolBar = QToolBar(self, floatable=False, movable=False, objectName="leftToolBar")
        explorerIcon = QIcon(":/images/explorer")
        explorerAction = QAction(explorerIcon, "Explorer", self)

        searchIcon = QIcon(":/images/search")
        searchAction = QAction(searchIcon, "Search", self)

        sourceControlIcon = QIcon(":/images/source_control")
        sourceControlAction = QAction(sourceControlIcon, "Source control", self)

        debugIcon = QIcon(":/images/debug")
        debugAction = QAction(debugIcon, "Debug", self)

        leftToolBar.addAction(explorerAction)
        leftToolBar.addAction(searchAction)
        leftToolBar.addAction(sourceControlAction)
        leftToolBar.addAction(debugAction)
        self.addToolBar(Qt.LeftToolBarArea, leftToolBar)

    def initUI(self):
        self.setWindowTitle("VSCode Demo")
        self.setStyleSheet(read_style('./style.css'))
        self.initToolbar()
        hsplitter = QSplitter(self)
        left = QListView()

        vsplitter = QSplitter(self, orientation=Qt.Vertical)
        rightTop = QTreeView()
        rightBottom = QTextEdit()
        vsplitter.addWidget(rightTop)
        vsplitter.addWidget(rightBottom)

        hsplitter.addWidget(left)
        hsplitter.addWidget(vsplitter)

        self.setCentralWidget(hsplitter)

        self.setGeometry(300, 300, 640, 480)
        self.show()


import sys

app = QApplication(sys.argv)
window = MainWindow()
sys.exit(app.exec_())
