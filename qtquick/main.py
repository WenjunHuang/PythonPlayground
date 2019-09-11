import random

from PySide2.QtWidgets import QApplication
from PySide2.QtQml import QQmlApplicationEngine
from PySide2.QtQuick import QQuickView
from PySide2.QtCore import QUrl, QObject, Signal, Slot

import sys


class NumberGenerator(QObject):
    nextNumber = Signal(int)

    def __init__(self):
        super().__init__()

    @Slot()
    def giveNumber(self):
        self.nextNumber.emit(random.randint(0, 99))


app = QApplication(sys.argv)
engine = QQmlApplicationEngine()

number_generator = NumberGenerator()
engine.rootContext().setContextProperty("numberGenerator",number_generator)
engine.load(QUrl("view.qml"))

if not engine.rootObjects():
    sys.exit(-1)
sys.exit(app.exec_())
