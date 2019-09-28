from PyQt5.QtCore import QObject, pyqtProperty, pyqtSignal
from PyQt5.QtWidgets import QLineEdit


class LineEditExtension(QObject):
    marginsChanged = pyqtSignal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self._lineedit = QLineEdit(parent)

    @pyqtProperty(int, notify=marginsChanged)
    def leftMargin(self) -> int:
        l, r, t, b = self._lineedit.getTextMargins()
        return l

    @leftMargin.setter
    def leftMargin(self, value: int) -> None:
        l, r, t, b = self._lineedit.getTextMargins()
        self._lineedit.setTextMargins(value, t, r, b)

    @pyqtProperty(int, notify=marginsChanged)
    def rightMargin(self) -> int:
        l, r, t, b = self._lineedit.getTextMargins()
        return r

    @rightMargin.setter
    def rightMargin(self, value: int) -> None:
        l, r, t, b = self._lineedit.getTextMargins()
        self._lineedit.setTextMargins(l, value, t, b)

    @pyqtProperty(int, notify=marginsChanged)
    def topMargin(self) -> int:
        l, r, t, b = self._lineedit.getTextMargins()
        return t

    @topMargin.setter
    def topMargin(self, value: int) -> None:
        l, r, t, b = self._lineedit.getTextMargins()
        self._lineedit.setTextMargins(l, r, value, b)

    @pyqtProperty(int, notify=marginsChanged)
    def bottomMargin(self) -> int:
        l, r, t, b = self._lineedit.getTextMargins()
        return b

    @topMargin.setter
    def bottomMargin(self, value: int) -> None:
        l, r, t, b = self._lineedit.getTextMargins()
        self._lineedit.setTextMargins(l, r, t, value)
