import sys

from PyQt5.QtCore import QUrl
from PyQt5.QtQml import QQmlEngine, QQmlApplicationEngine
from PyQt5.QtWidgets import QApplication

app = QApplication(sys.argv)
engine = QQmlApplicationEngine()
engine.load(QUrl("./scrollview.qml"))

if not engine.rootObjects():
    sys.exit(-1)
sys.exit(app.exec_())
