import sys

from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWebEngineWidgets import *

app = QApplication(sys.argv)
pv = QWebEngineView()
pv.setUrl(QUrl("http://www.baidu.com"))
pv.show()
sys.exit(app.exec_())
