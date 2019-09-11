import random
import sys
from PySide2.QtCore import QObject, Signal, Slot, QUrl
from PySide2.QtGui import QGuiApplication
from PySide2.QtQml import QQmlApplicationEngine


class NumberGenerator(QObject):
    nextNumber = Signal(int, arguments=['number'])

    def __init__(self):
        super().__init__()

    @Slot()
    def giveNumber(self):
        self.nextNumber.emit(random.randint(0, 99))


if __name__ == '__main__':
    app = QGuiApplication(sys.argv)
    engine = QQmlApplicationEngine()

    number_generator = NumberGenerator()
    engine.rootContext().setContextProperty("numberGenerator", number_generator)
    engine.load(QUrl("number_generator.qml"))

    if not engine.rootObjects():
        sys.exit(-1)
    sys.exit(app.exec_())
