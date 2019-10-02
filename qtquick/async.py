import functools
import sys
import asyncio
import aiohttp
from PyQt5.QtCore import QUrl, QObject, pyqtSlot, pyqtProperty
from PyQt5.QtQml import QQmlApplicationEngine, QJSValue, qjsEngine, qmlRegisterType, QQmlEngine
from PyQt5.QtQuick import QQuickItem
from asyncqt import QEventLoop, asyncSlot, asyncClose
from PyQt5.QtGui import QGuiApplication
from typing import List


def myAsyncSlot(*args):
    """Make a Qt async slot run on asyncio loop."""

    def outer_decorator(fn):
        @pyqtSlot(*args)
        @functools.wraps(fn)
        def wrapper(*args, **kwargs):
            asyncio.ensure_future(fn(*args, **kwargs))

        return wrapper

    return outer_decorator


class Http(QObject):
    def __init__(self):
        super().__init__()
        self.session = aiohttp.ClientSession(
            loop=asyncio.get_event_loop())

    @pyqtSlot(QJSValue, QJSValue)
    def fetch(self, exported: QJSValue, callback: QJSValue):
        obj = exported.toQObject()
        if isinstance(obj, Exported):
            print('ok')
        asyncio.create_task(self.async_fetch(obj.url, QJSValue(callback)))

    async def async_fetch(self, url, callback: QJSValue):
        try:
            async with self.session.get(url) as r:
                result = await r.text()

        except Exception as e:
            result = f"Error: {e}"
        print(result)

        engine = qjsEngine(self)
        result_object = engine.newObject()
        result_object.setProperty("result", QJSValue(result))
        # result = [QJSValue(result)]
        result = [result_object]
        callback.call(result)


class Exported(QObject):
    def __init__(self, url):
        super().__init__()
        self._url = url

    @pyqtProperty(str)
    def url(self):
        return self._url


class ExportedFactory(QObject):
    def __init__(self):
        super().__init__()

    @pyqtSlot(str, result=QJSValue)
    def create(self, url: str):
        rtn = Exported(url)
        return engine.newQObject(rtn)


class Foo(QQuickItem):
    def __init__(self, parent=None):
        super().__init__(parent)
        self._name = None

    @pyqtProperty(str)
    def item(self):
        return self._name

    @item.setter
    def item(self, value: str):
        self._name = value
        ctx = QQmlEngine.contextForObject(self)
        print(ctx.baseUrl())


app = QGuiApplication(sys.argv)
engine = QQmlApplicationEngine()
qmlRegisterType(Foo, 'Foo', 1, 0, 'Foo')
# qmlRegisterType(ExportedFactory, 'Exported', 1, 0, 'ExportedFactory')
loop = QEventLoop(app)
asyncio.set_event_loop(loop)

http = Http()
engine.rootContext().setContextProperty("http", http)

exported_factory = ExportedFactory()
engine.rootContext().setContextProperty('exportedFactory', exported_factory)

# exported = engine.newQMetaObject(Exported.staticMetaObject)
# js_global = engine.globalObject()
# js_global.setProperty("Exported", exported)

engine.load(QUrl("async.qml"))
if not engine.rootObjects():
    sys.exit(-1)

asyncio.events._set_running_loop(loop)
with loop:
    sys.exit(loop.run_forever())
