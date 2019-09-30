import functools
import sys
import asyncio
import aiohttp
from PyQt5.QtCore import QUrl, QObject, pyqtSlot
from PyQt5.QtQml import QQmlApplicationEngine, QJSValue, qjsEngine
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

    @pyqtSlot(str, QJSValue)
    def fetch(self, url: str, callback: QJSValue):
        asyncio.create_task(self.async_fetch(url, QJSValue(callback)))

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


app = QGuiApplication(sys.argv)
engine = QQmlApplicationEngine()
loop = QEventLoop(app)
asyncio.set_event_loop(loop)

http = Http()
engine.rootContext().setContextProperty("http", http)

engine.load(QUrl("async.qml"))
if not engine.rootObjects():
    sys.exit(-1)

asyncio.events._set_running_loop(loop)
with loop:
    sys.exit(loop.run_forever())
