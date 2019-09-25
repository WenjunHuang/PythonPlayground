import sys
import random
from typing import Optional

from PyQt5.QtGui import QGuiApplication
from PyQt5.QtQml import QQmlApplicationEngine, qmlRegisterType
from PyQt5.QtCore import QObject, QUrl, pyqtSignal, pyqtSlot, pyqtProperty
from dataclasses import dataclass

from dataclasses_json import dataclass_json


class NumberGenerator(QObject):
    def __init__(self, parent=None):
        super().__init__(parent)

    nextNumber = pyqtSignal(int, arguments=['number'])

    @pyqtSlot(name='giveNumber')
    def give_number(self):
        self.nextNumber.emit(random.randint(0, self._max))

    @pyqtProperty(int)
    def max(self):
        return self._max

    @max.setter
    def max(self, value: int):
        self._max = value


class RawData(QObject):
    @pyqtProperty(int)
    def max(self) -> Optional[int]:
        return self._max

    @max.setter
    def max(self, value: int):
        self._max = value


    # def __init__(self):
    #     super().__init__()


if __name__ == '__main__':
    app = QGuiApplication(sys.argv)
    engine = QQmlApplicationEngine()

    raw_json = '{"max":100}'
    data = RawData(max=100)
    qmlRegisterType(NumberGenerator, 'Generators', 1, 0, 'NumberGenerator')
    engine.rootContext().setContextProperty("rawData", data)
    engine.load(QUrl('number_generator_expose_python_to_qml.qml'))

    if not engine.rootObjects():
        sys.exit(-1)

    sys.exit(app.exec_())
