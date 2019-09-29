from PyQt5.QtCore import QAbstractTableModel, QModelIndex, pyqtProperty, pyqtSignal, Qt, QVariant, QSize
from PyQt5.QtGui import QImage, qGray
from typing import Any


class ImageModel(QAbstractTableModel):
    sourceChanged = pyqtSignal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self._source = ""
        self._image = QImage()

    @pyqtProperty(str, notify=sourceChanged)
    def source(self) -> str:
        return self._source

    @source.setter
    def source(self, value: str):
        if self._source == value:
            return

        self.beginResetModel()
        self._source = value
        self._image.load(self._source)
        self.endResetModel()

    def rowCount(self, parent: QModelIndex = QModelIndex()) -> int:
        if parent.isValid():
            return 0
        return self._image.height()

    def columnCount(self, parent: QModelIndex = QModelIndex()) -> int:
        if parent.isValid():
            return 0
        return self._image.width()

    def data(self, index: QModelIndex, role: int) -> Any:
        if not index.isValid() or role != Qt.DisplayRole:
            return QVariant()
        return qGray(self._image.pixel(index.column(), index.row()))

    def headerData(self, section: int, orientation: Qt.Orientation, role: int) -> Any:
        if role == Qt.SizeHintRole:
            return QSize(1, 1)
        return QVariant()
