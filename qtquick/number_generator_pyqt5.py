import random
import sys
from PyQt5.QtGui import QGuiApplication
from PyQt5.QtCore import QObject, pyqtSignal, pyqtSlot, QUrl
from PyQt5.QtQml import QQmlApplicationEngine


class NumberGeneratorPyQt5(QObject):
    nextNumber = pyqtSignal(int, name='nextNumber', arguments=['number'])

    def __init__(self):
        super().__init__()

    @pyqtSlot()
    def giveNumber(self):
        self.nextNumber.emit(random.randint(0, 100))


if __name__ == '__main__':
    app = QGuiApplication(sys.argv)
    engine = QQmlApplicationEngine()

    number_generator = NumberGeneratorPyQt5()
    engine.rootContext().setContextProperty("numberGenerator", number_generator)
    engine.load(QUrl("number_generator_pyqt5.qml"))

    if not engine.rootObjects():
        sys.exit(-1)
    sys.exit(app.exec_())
