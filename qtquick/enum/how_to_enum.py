from enum import IntEnum
import sys

from PyQt5.QtCore import Q_ENUM, QObject
from PyQt5.QtQml import QQmlApplicationEngine, qmlRegisterType, qmlRegisterUncreatableType
from PyQt5.QtWidgets import QApplication


class Kind(IntEnum):
    Foo, Bar = range(2)

class Foo(QObject):
    Q_ENUM(Kind)


app = QApplication(sys.argv)
qmlRegisterUncreatableType(Foo, "Test", 1, 0, "Kind", "Not creatable")
engine = QQmlApplicationEngine()
engine.load('./enum.qml')

sys.exit(app.exec_())
