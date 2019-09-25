import functools
import sys
import asyncio
import aiohttp
from PyQt5.QtCore import QUrl, QObject, pyqtSlot
from PyQt5.QtQml import QQmlApplicationEngine, QJSValue, qjsEngine
from asyncqt import QEventLoop, asyncSlot, asyncClose
from PyQt5.QtGui import QGuiApplication


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
        asyncio.ensure_future(self.async_fetch(url, QJSValue(callback)))

    async def async_fetch(self, url, callback: QJSValue):
        try:
            async with self.session.get(url) as r:
                result = await r.text()

            await asyncio.sleep(10)
        except Exception as e:
            result = f"Error: {e}"

        result = [QJSValue(result)]
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

with loop:
    sys.exit(loop.run_forever())
