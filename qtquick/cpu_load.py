import sys
import psutil

from PySide2.QtGui import QGuiApplication
from PySide2.QtQml import QQmlApplicationEngine, qmlRegisterType
from PySide2.QtCore import QUrl, QTimer, QAbstractListModel
from PySide2.QtCore import QObject, Signal, Slot, Property, Qt, QModelIndex


class CpuLoadModel(QAbstractListModel):
    def __init__(self):
        super().__init__()

        self.__cpu_count = psutil.cpu_count()
        self.__cpu_load = [0] * self.__cpu_count

        self.__update_timer = QTimer(self)
        self.__update_timer.setInterval(1000)
        self.__update_timer.timeout.connect(self.__update)
        self.__update_timer.start()

        psutil.cpu_percent(percpu=True)

    def __update(self):
        self.__cpu_load = psutil.cpu_percent(percpu=True)
        self.dataChanged.emit(self.index(0, 0), self.index(self.__cpu_count - 1, 0))

    def rowCount(self, parent: QModelIndex) -> int:
        return self.__cpu_count

    def data(self, index: QModelIndex, role: int) -> any:
        if (role == Qt.DisplayRole and
                0 <= index.row() < len(self.__cpu_load) and
                index.column() == 0):
            return self.__cpu_load[index.row()]
        else:
            return None


def main():
    app = QGuiApplication(sys.argv)
    engine = QQmlApplicationEngine()

    qmlRegisterType(CpuLoadModel, 'PsUtils', 1, 0, 'CpuLoadModel')
    engine.load(QUrl('cpu.qml'))

    if not engine.rootObjects():
        sys.exit(-1)

    sys.exit(app.exec_())


main()
