from PyQt5.QtCore import QObject, pyqtSignal, pyqtProperty, pyqtSlot


class Foo(QObject):
    nameChanged = pyqtSignal()

    def __init__(self):
        super().__init__()

    @pyqtProperty(str, notify=nameChanged)
    def name(self):
        return self._name

    @name.setter
    def name(self, value: str):
        self._name = value
        self.nameChanged.emit()


class Bar(QObject):
    def __init__(self):
        super().__init__()

    @pyqtSlot()
    def my_slot(self):
        print("property changed")


f = Foo()
b = Bar()
f.nameChanged.connect(b.my_slot)

f.name = "wenjun"
