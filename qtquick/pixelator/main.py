import sys

from PyQt5.QtCore import QUrl
from PyQt5.QtGui import QGuiApplication
from PyQt5.QtQml import QQmlApplicationEngine, qmlRegisterType
from imagemodel import ImageModel

app = QGuiApplication(sys.argv)
engine = QQmlApplicationEngine()
qmlRegisterType(ImageModel, "ImageModel", 1, 0, 'ImageModel')
engine.load(QUrl("./main.qml"))
if not engine.rootObjects():
    sys.exit(-1)

sys.exit(app.exec_())
