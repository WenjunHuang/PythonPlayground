from PyQt5.QtCore import QRect, Qt, QCoreApplication, QSize, QRectF, QPointF
from PyQt5.QtGui import QColor, QBrush, QLinearGradient, QPainter, QGuiApplication, QPixmapCache, QPixmap, QPolygonF, \
    QPalette, QPen
from PyQt5.QtWidgets import QCommonStyle, QStyleOption, QStyleOptionComplex, QStyleOptionSpinBox, qApp, \
    QStyleOptionTitleBar
from enum import Enum
from platform import platform


class Direction(Enum):
    TopDown = 1,
    FromLeft = 2,
    BottomUp = 3,
    FromRight = 4


kWindowsItemFrame = 2
kWindowsItemHMargin = 3
kWindowsItemVMargin = 8
kWindowsRightBorder = 15


def merged_colors(colorA: QColor, colorB: QColor, factor: int = 50) -> QColor:
    max_factor = 100
    tmp = QColor()
    tmp.setRed((colorA.red() * factor) // max_factor + (colorB.red() * (max_factor - factor)) // max_factor)
    tmp.setGreen((colorA.green() * factor) // max_factor + (colorB.green() * (max_factor - factor)) // max_factor)
    tmp.setBlue((colorA.blue() * factor) // max_factor + (colorB.blue() * (max_factor - factor)) // max_factor)

    return tmp


def qt_fusion_gradient(rect: QRect, base_color: QBrush, direction: Direction = Direction.TopDown) -> QLinearGradient:
    x = rect.center().x()
    y = rect.center().y()

    gradient = None
    if direction == Direction.FromLeft:
        gradient = QLinearGradient(rect.left(), y, rect.right(), y)
    elif direction == Direction.FromRight:
        gradient = QLinearGradient(rect.right(), y, rect.left(), y)
    elif direction == Direction.BottomUp:
        gradient = QLinearGradient(x, rect.bottom(), x, rect.top())
    else:
        gradient = QLinearGradient(x, rect.top(), x, rect.bottom())

    if base_color.gradient():
        gradient.setStops(base_color.gradient().stops())
    else:
        start_color = base_color.color().lighter(124)
        stop_color = base_color.color().lighter(102)
        gradient.setColorAt(0, start_color)
        gradient.setColorAt(1, stop_color)

    return gradient


def qt_defaultDpiX():
    if QCoreApplication.instance().testAttribute(Qt.AA_Use96Dpi):
        return 96

    screen = QGuiApplication.primaryScreen()
    if screen:
        return round(screen.logicalDotsPerInch())
    return 100


def dpi_scaled(value):
    if platform() == 'MacOS':
        return value
    else:
        scale = qt_defaultDpiX() / 96
        return value * scale


def unique_name(key: str, option: QStyleOption, size: QSize) -> str:
    complex_option = (QStyleOptionComplex)(option) if isinstance(option, QStyleOptionComplex) else None

    tmp = key + hex(option.state).lstrip("0x") + hex(option.direction).lstrip("0x") + hex(
        complex_option.activeSubControls if complex_option else 0).lstrip("0x") + hex(option.palette.cacheKey()).lstrip(
        "0x") + hex(size.width()).lstrip("0x") + hex(size.height()).lstrip("0x")

    if isinstance(option, QStyleOptionSpinBox):
        spin_box = (QStyleOptionSpinBox)(option)
        tmp = tmp + hex(spin_box.buttonSymbols).lstrip("0x") + hex(spin_box.stepEnabled).lstrip("0x") + (
            "1" if spin_box.frame else "0")

    return tmp


def style_cache_pixmap(size: QSize) -> QPixmap:
    pixel_ratio = qApp.devicePixelRatio()
    cache_pixmap = QPixmap(size * pixel_ratio)
    cache_pixmap.setDevicePixelRatio(pixel_ratio)
    return cache_pixmap


def qt_fusion_draw_arrow(type: Qt.ArrowType, painter: QPainter, option: QStyleOption, rect: QRect,
                         color: QColor) -> None:
    if rect.isEmpty():
        return
    arrow_width = dpi_scaled(14)
    arrow_height = dpi_scaled(8)

    arrow_max = min(arrow_height, arrow_width)
    rect_max = min(rect.height(), rect.width())
    size = min(arrow_max, rect_max)

    cache_key = unique_name("fusion-arrow", option, rect.size()) + hex(type).lstrip("0x") + hex(color.rgba()).lstrip(
        "0x")

    cache_pixmap = QPixmapCache.find(cache_key)
    if not cache_pixmap:
        cache_pixmap = style_cache_pixmap(rect.size())
        cache_pixmap.fill(Qt.transparent)
        cache_painter = QPainter(cache_pixmap)

        arrow_rect = QRectF()
        arrow_rect.setWidth(size)
        arrow_rect.setHeight(arrow_height * size / arrow_width)
        if type == Qt.LeftArrow or type == Qt.RightArrow:
            arrow_rect = arrow_rect.transposed()
        arrow_rect.moveTo((rect.width() - arrow_rect.width()) / 2.0, (rect.height() - arrow_rect.height()) / 2.0)

        triangle = QPolygonF()
        triangle.reserve(3)

        if type == Qt.DownArrow:
            triangle << arrow_rect.topLeft() << arrow_rect.topRight() << QPointF(arrow_rect.center().x(),
                                                                                 arrow_rect.bottom())
        elif type == Qt.RightArrow:
            triangle << arrow_rect.topLeft() << arrow_rect.bottomLeft() << QPointF(arrow_rect.right(),
                                                                                   arrow_rect.center().y())
        elif type == Qt.LeftArrow:
            triangle << arrow_rect.topRight() << arrow_rect.bottomRight() << QPointF(arrow_rect.left(),
                                                                                     arrow_rect.center().y())
        else:
            triangle << arrow_rect.bottomLeft() << arrow_rect.bottomRight() << QPointF(arrow_rect.center().x(),
                                                                                       arrow_rect.top())

        cache_painter.setPen(Qt.NoPen)
        cache_painter.setBrush(color)
        cache_painter.setRenderHint(QPainter.Antialiasing)
        cache_painter.drawPolygon(triangle)

        QPixmapCache.insert(cache_key, cache_pixmap)

    painter.drawPixmap(rect, cache_pixmap)

def qt_fusion_draw_midbutton(painter:QPainter,option:QStyleOptionTitleBar,tmp:QRect,hover:bool,sunken:bool):
    
class FooStyle(QCommonStyle):
    def __init__(self):
        super().__init__()
        self.setObjectName("Foo")

    def drawItemText(self, painter: QPainter, rectangle: QRect, alignment: int, palette: QPalette, enabled: bool,
                     text: str, textRole: QPalette.ColorRole) -> None:
        if not text:
            return

        saved_pen = painter.pen()
        if textRole != QPalette.NoRole:
            painter.setPen(QPen(palette.brush(textRole),saved_pen.widthF()))
