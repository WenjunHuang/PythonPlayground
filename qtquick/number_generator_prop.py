import random
import sys
from PyQt5.QtCore import QObject, pyqtSignal, pyqtSlot, pyqtProperty, QUrl
from PyQt5.QtGui import QGuiApplication
from PyQt5.QtQml import QQmlApplicationEngine


class NumberGenerator(QObject):

    def __init__(self):
        super().__init__()
        self.__number = 42
        self.__max_number = 99

    def number(self) -> int:
        return self.__number

    def __set_number(self, val: int) -> None:
        if self.__number != val:
            self.__number = val
            self.numberChanged.emit(self.__number)

    numberChanged = pyqtSignal(int, arguments=['number'])
    number = pyqtProperty(int, fget=number, notify=numberChanged)

    def max_number(self) -> int:
        return self.__max_number

    def set_max_number(self, val: int) -> None:
        if val < 0:
            val = 0

        if self.__max_number != val:
            self.__max_number = val
            self.maxNumberChanged.emit()

        if self.__number > self.__max_number:
            self.__set_number(self.__max_number)

    maxNumberChanged = pyqtSignal()
    maxNumber = pyqtProperty(int, fget=max_number, fset=set_max_number, notify=maxNumberChanged)

    @pyqtSlot(name="updateNumber")
    def update_number(self) -> None:
        self.__set_number(random.randint(0, self.__max_number))


if __name__ == '__main__':
    app = QGuiApplication(sys.argv)
    engine = QQmlApplicationEngine()

    number_generator = NumberGenerator()
    number_generator.maxNumber = 50
    engine.rootContext().setContextProperty("numberGenerator", number_generator)
    engine.load(QUrl("number_generator_prop.qml"))

    if not engine.rootObjects():
        sys.exit(-1)

    sys.exit(app.exec_())
