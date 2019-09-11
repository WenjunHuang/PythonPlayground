from PySide2.QtSql import QSqlRelationalDelegate
from PySide2.QtWidgets import QItemDelegate, QSpinBox, QStyledItemDelegate, QStyle, QStyleOptionViewItem, QWidget
from PySide2.QtGui import QMouseEvent, QPixmap, QPalette, QPainter
from PySide2.QtCore import QEvent, QSize, Qt, QModelIndex, QAbstractItemModel


class BookDelegate(QSqlRelationalDelegate):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.star = QPixmap(":/images/star.png")

    def paint(self, painter: QPainter, option: QStyleOptionViewItem, index: QModelIndex):
        if index.column() != 5:
            opt = option
            opt.rect.adjust(0, 0, -1, -1)
            QSqlRelationalDelegate.paint(self, painter, opt, index)
        else:
            model = index.model()
            if option.state & QStyle.State_Enabled:
                if option.state & QStyle.State_Active:
                    color_group = QPalette.Normal
                else:
                    color_group = QPalette.Inactive
            else:
                color_group = QPalette.Disabled

            if option.state & QStyle.State_Selected:
                painter.fillRect(option.rect,
                                 option.palette.color(color_group, QPalette.Highlight))
            rating = model.data(index, Qt.DisplayRole)
            width = self.star.width()
            height = self.star.height()
            x = option.rect.x()
            y = option.rect.y() + (option.rect.height() / 2) - (height / 2)
            for i in range(rating):
                painter.drawPixmap(x, y, self.star)
                x += width

            self.drawFocus(painter, option, option.rect.adjusted(0, 0, -1, -1))

        pen = painter.pen()
        painter.setPen(option.palette.color(QPalette.Mid))
        painter.drawLine(option.rect.bottomLeft(), option.rect.bottomRight())
        painter.drawLine(option.rect.topRight(), option.rect.bottomRight())
        painter.setPen(pen)

    def sizeHint(self, option: QStyleOptionViewItem, index: QModelIndex) -> QSize:
        if index.column() == 5:
            size_hint = QSize(5 * self.star.width(), self.star.height()) + QSize(1, 1)
            return size_hint
        return QSqlRelationalDelegate.sizeHint(self, option, index) + QSize(1, 1)

    def editorEvent(self, event: QEvent, model: QAbstractItemModel, option: QStyleOptionViewItem,
                    index: QModelIndex) -> bool:
        if index.column() != 5:
            return False

        if event.type() == QEvent.MouseButtonPress:
            mouse_pos = event.pos()
            new_stars = int(0.7 + (mouse_pos.x() - option.rect.x()) / self.star.width())
            stars = max(0, min(new_stars, 5))
            model.setData(index, stars)
            return False

        return True

    def createEditor(self, aParent: QWidget, option: QStyleOptionViewItem, index: QModelIndex) -> QWidget:
        if index.column() != 4:
            return QSqlRelationalDelegate.createEditor(self,
                                                       aParent,
                                                       option,
                                                       index)
        spinbox = QSpinBox(aParent)
        spinbox.setFrame(False)
        spinbox.setMaximum(2100)
        spinbox.setMinimum(-1000)
        return spinbox
