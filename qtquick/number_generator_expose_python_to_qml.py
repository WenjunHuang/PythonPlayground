import sys
import random
from PyQt5.QtGui import QGuiApplication
from PyQt5.QtQml import QQmlApplicationEngine, qmlRegisterType
from PyQt5.QtCore import QObject, QUrl, pyqtSignal, pyqtSlot


class NumberGenerator(QObject):
    def __init__(self, parent=None):
        super().__init__(parent)

    nextNumber = pyqtSignal(int, arguments=['number'])

    @pyqtSlot(name='giveNumber')
    def give_number(self):
        self.nextNumber.emit(random.randint(0, 99))


if __name__ == '__main__':
    app = QGuiApplication(sys.argv)
    engine = QQmlApplicationEngine()

    qmlRegisterType(NumberGenerator, 'Generators', 1, 0, 'NumberGenerator')
    engine.load(QUrl('number_generator_expose_python_to_qml.qml'))

    if not engine.rootObjects():
        sys.exit(-1)

    sys.exit(app.exec_())
